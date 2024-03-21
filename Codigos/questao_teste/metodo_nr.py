from math import fabs

def nr(função, derivada, x0, tol, inter):

    for i in range(1,inter + 1):
        if(fabs(função(x0)) <= tol): return x0
        x0 = x0 - função(x0)/derivada(x0)
    return None
                  
                  
lucas
