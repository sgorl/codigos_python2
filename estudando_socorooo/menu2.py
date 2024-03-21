import agenda_2

def main():
    while True:
        print(" contatos da agenda")
        print(" adicionar um contato: 1")
        print(" remover um contato: 2")
        print(" editar um contato: 3")
        print(" procurar um contato: 4")
        print(" mostrar os contatos salvos: 5")
        print(" sair: 6")

        choice = int(input("digite a opção:"))

        if choice == 1:
            nome = input("digite o nome:")
            numero = str(input("digite o numero:"))
            agenda_2.adicionar_contato(nome,numero)
        if choice == 2:
            nome = input("digite o nome do contato a ser removido:")
            agenda_2.remover_contato(nome)
        if choice == 3:
            nome = input("digite o nome do contato a ser editado:")
            novo_numero = int(input("digite o novo numero"))
            agenda_2.editar_contato(nome, novo_numero)
        if choice == 4:
            nome = input("digite o nome do contato:")
            agenda_2.procurar_contato(nome)
        if choice == 5:
            agenda_2.mostrar_contatos()
        if choice == 6:
            break
main()