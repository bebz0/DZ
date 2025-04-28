import math

def generate_xk(x):
    k = 0
    current = 1
    while True:
        yield current
        k += 1
        current *= x**2 / ((2*k - 1)*(2*k))

x = 1
k = 3
gen = generate_xk(x)
for _ in range(k + 1):
    value = next(gen)
print(f"x_{k} = {value}")

#---------------------------------

def generate_Pn():
    n = 1
    cur = 1
    while True:
        cur *= (1 + 1/(n**2))
        yield cur
        n += 1


n = 5
gen = generate_Pn()
for _ in range(n):
    value = next(gen)
print(f"P_{n} = {value}")


#---------------------------------


def generate_determinant(a, b):
    D1 = a + b
    D2 = (a+b)**2 - (a*b)**2
    yield D1
    yield D2
    while True:
        D_next = (a+b)*D2 - (a*b)**2*D1
        yield D_next
        D1, D2 = D2, D_next


n = 3
a = 1
b = 2
gen = generate_determinant(a, b)
for _ in range(n):
    det = next(gen)
print(f"Дет для n={n}: {det}")


#---------------------------------


def generate_ak():
    a1 = a2 = a3 = 1
    yield a1
    yield a2
    yield a3
    while True:
        ak = a3 + a1
        yield ak
        a1, a2, a3 = a2, a3, ak


def calculate_Sn(n):
    gen = generate_ak()
    S = 0
    for k in range(1, n+1):
        ak = next(gen)
        S += ak / (2**k)
    return S

n = 5
Sn = calculate_Sn(n)
print(f"S_{n} = {Sn}")


#---------------------------------


def generate_taylor(x):
    n = 1
    term = 2 * x
    while True:
        yield term
        n += 2
        term = 2 * (x**n) / n


def taylor_ln(x, e=1e-6):
    assert abs(x) < 1
    gen = generate_taylor(x)
    result = 0
    term = next(gen)
    while abs(term) > e:
        result += term
        term = next(gen)
    return result

x = 0.5
e = 1e-6
res = taylor_ln(x, e)
real = math.log((1+x)/(1-x))
print(f"Результат: {res}")
print(f"З бібліотеки): {real}")
print(f"Різниця: {abs(res - real)}")