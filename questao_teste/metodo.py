from math import fabs
def bi(função, lista_coeficientes, a, b, tol, inter):

    if(fabs(função(lista_coeficientes, a)) <= tol): return a
    if(fabs(função(lista_coeficientes, b)) <= tol): return b
    if((função(lista_coeficientes, a))*função(lista_coeficientes, b) > 0): 
        print(" there is no root here ")
        return None
    for i in range(1,inter + 1):
        x = (a + b)/2
        if(fabs(função(lista_coeficientes,x)) < tol): break
        if(função(lista_coeficientes, x)*função(lista_coeficientes, b) > 0):
            b = x
        else:
            a = x
    return x    

def nr(função, derivada, x0, tol, inter):

    for i in range(1,inter + 1):
        if(fabs(função(x0)) <= tol): return x0
        x0 = x0 - função(x0)/derivada(x0)
    return None
               
def função(lista_coeficientes, x):
    y = 0 
    for i in range(0,len(lista_coeficientes)):
        y = y + lista_coeficientes[i]*x**i
    return y

def print_função(lista_coeficientes):
    função_printada = "f(x) = "
    for i in range(len(lista_coeficientes) - 1, -1, -1):
        if(lista_coeficientes[i] >= 0):
            função_printada = função_printada + "+" + str(lista_coeficientes[i]) + "x^" + str(i) + " "
        else:
            função_printada = função_printada + str(lista_coeficientes[i]) + "x^" + str(i) + " "
        # f(x) = 2x - 2
    return função_printada


    