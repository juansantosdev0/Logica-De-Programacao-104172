import os

lista_filmes = []

while True:
    os.system("cls")

    print('''
1 - cadastrar filme
2 - listar filmes
0 - sair
''')

    opcao = int(input("Escolha uma Opção: "))

    match opcao:
        case 1:
            print("\n== CADASTRAR UM FILME ==")
            if len(lista_filmes) >= 5:
                print("A lista ja atingiu o limite de 5 filmes!")
            else:
                nome = input("Nome do novo Filme: ").strip().upper()
                if nome == '':
                    print("O nome nao pode ficar vazio. ")
                elif nome in lista_filmes:
                    print(f"{nome} Ja esta cadastrado. ")
                else:
                    lista_filmes.append(nome)
                    print("Filme Cadastrado com Sucesso! ")
            
            input("presione uma tecla para continuar...")

        case 2:
            print("\n== FILMES NA LISTA ==")
            if len(lista_filmes) == 0:
                print("A lista esta vazia")
            else:
                for i, filme in enumerate(lista_filmes):
                    print(f"{i+1}. {filme}")
                
                print(f"Total de filmes: {len(lista_filmes)}")
            
            input("presione uma tecla para continuar...")

        case 0:
            print("FIM DO PROGRAMA. ")
            break

        case _:
            print("Opção invalida")
            input("presione uma tecla para continuar...")