import os

lista_produtos = []

while True:
    os.system("cls")
    input("presione uma tecla para continuar...")
    print('''
1 - cadastrar produtos
2 - listar produtos
0 - sair
''')

    opcao = int(input("Escolha uma Opção: "))

    match opcao:
        case 1:
            print("\n== CADASTRAR UM PRODUTO ==")
            nome = input("Nome de novo Produto: ").strip().upper()
            if nome == '':
                print("O nome nao pode ficar vazio. ")
            elif nome in lista_produtos:
                print(f"{nome} Ja estar cadastrado. ")
            else:
                lista_produtos.append(nome)
            print("Produto Cadastrado com Sucesso! ")
            input("presione uma tecla para continuar...")

        case 2:
            print("\n== produto no estoque ==")
            if len(lista_produtos) == 0:
                print("O estoque estar vazio")
            else:
                for i, produto in enumerate(lista_produtos):
                    print(f"{i+1}. {produto}")
                    print(f"Total de produtos: {len(lista_produtos)}")
                    input("presione uma tecla para continuar...")
        case 0:
            print("FIM DO PROGRAMA. ")
            break
        case _:
            print("Opção invalida")
            input("presione uma tecla para continuar...")