lista_coeficientes = []
"""
gf = int(input("digite o grau da função: "))

for i in range(0,gf):
    lista_coeficientes.append(float(input("digite o coeficiente de grau {i}: ")))
"""
def função(lista_coefientes, x):
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
