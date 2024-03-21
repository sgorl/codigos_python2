contatos = {}


def adicionar_contato(nome, numero):
    #contatos[nome] = numero
    texto = open("texto.txt", "a+")
    texto.write(nome + " " + numero + "\n")
    texto.close()
    print(f"contato {nome} adcionado")

def remover_contato(nome):
    if nome in contatos:
        del contatos[nome]
        print(f"contato {nome} foi removido ")
    else:
        print(f"contato {nome} não exite")

def editar_contato(nome, novo_numero):
    if nome in contatos:
        contatos[nome] = novo_numero
        print(f"o contato de {nome} foi editado para {novo_numero}")
    else:
        print(f" o contato de {nome} não existe")

def procurar_contato(nome):
    if nome in contatos:
        print(f"{contatos[nome]}")
    else:
        print(f"contato {nome} não existe")

def mostrar_contatos():
    if contatos:
        print("os contatos são: ")
        for nome, numero in contatos.items():
            print(f"{nome} e {numero}")
