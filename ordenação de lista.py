lista_usuario = []
usuario = input("digite o que deseja armazenar\n")
lista_usuario.append(usuario)
x = True
while(x == True):
    escolha = int(input(" deseja armanezar outro item na lista? (1), deseja remover(2) ou sair do programa(3)"))
    if( escolha == 1 ):
        add = input("digite o item a ser adicionado\n")
        lista_usuario.append(add)
    elif( escolha == 2):
        print(lista_usuario)
        remover = int(input("qual o item deseja remover?"))
        lista_usuario.pop(remover)
    else:
        x = False
        
lista_usuario.sort()    
print(lista_usuario)

        




