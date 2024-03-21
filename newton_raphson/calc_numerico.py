
def nr(f, df, x0, epsilon, Iter):
    if abs(f(x0)) <= epsilon:
        return x0
    print("k\t x0\t\t f(x0)")
    k = 1
    while k <= Iter:
        x1 = x0 - f(x0)/df(x0)
        print("%d %e\t %e" %(k, x1, f(x1)))
        if abs(f(x1)) <= epsilon:
            return x1
        x0 = x1
        k = k + 1
        print("limite maximo de interações")
        return x1
    