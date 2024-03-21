lista_res = []
r1 = float(input("digite o primeiro valor de resistência"))
lista_res.append(r1) 
x = True

while x == True:
    r2 = float(input("digite o valor do segundo resitor"))
    lista_res.append(r2)
    var_escolha = int(input("os resistores estão em paralelo(1) ou serie(2)"))
    if (var_escolha == 1):
        rq = (r1*r2)/(r1+r2)
    else: 
        rq = r1+r2
    var_saida = int(input("desaja adicionar mais uma resistência? sim(1) e não(!=1)"))
    r1 = rq
    if (var_saida != 1):
        x = False
print(lista_res, rq)    


    
