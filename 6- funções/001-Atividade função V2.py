import os


def logo_senai():
    print("\n" + "=" * 15)
    print("       SENAI")
    print("=" * 15)


def cadastrar_cliente():
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    telefone = input("Digite o telefone: ")
    return nome, email, telefone


def mostrar_dados(nome, email, telefone):
    if not nome:
        print("\nNenhum cliente cadastrado ainda!")
    else:
        print(f"\nNome: {nome}")
        print(f"E-mail: {email}")
        print(f"Telefone: {telefone}")


nome, email, telefone = "", "", ""

while True:
    os.system("cls" if os.name == "nt" else "clear")
    logo_senai()
    print("1 - CADASTRAR CLIENTE")
    print("2 - MOSTRAR DADOS DO CLIENTE")
    print("3 - SAIR")

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            nome, email, telefone = cadastrar_cliente()
            input("\nCliente cadastrado com sucesso! Pressione Enter para voltar ao menu...")
        case "2":
            mostrar_dados(nome, email, telefone)
            input("\nPressione Enter para voltar ao menu...")
        case "3":
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção incorreta!")
            input("\nPressione Enter para tentar novamente...")