"""
Ache o valor aproximado da raiza da funçãopelo metodo de newton raphson
f(x) = x³ - 2x² - 5
f'(x) = 3x² - 4x
Epsilon = 0.001
n = 20
x₀ = 4

"""
from calc_numerico import*


def f(x):
    return x**3 - 2*x**2 - 5
def df(x):
    return 3*x**2 - 4*x

raiz = nr(f, df, 4, 0.001, 20)

print(raiz)
