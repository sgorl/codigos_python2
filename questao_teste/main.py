import metodo

lista_coeficientes = []

gf = int(input("digite o grau da função: "))

for i in range(0, gf):
    lista_coeficientes.append(float(input(f"digite o coenficiente de grau {i}: ")))
while True:
    print(" meteodo newton digite 1 ")
    print(" metedo bisseção 2")

    choice = int(input("escolha a o metodo: "))


    if(choice == 2):
        print("alouuu")
        print(metodo.bi(metodo.função, lista_coeficientes, -2, 2, 0.0002, 20))


