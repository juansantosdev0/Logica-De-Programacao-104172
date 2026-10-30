import os
os.system("cls")

elenco = []

while True:
    print("\n1. Cadastrar jogador")
    print("2. Listar jogadores")
    print("3. Atualizar jogador")
    print("4. Excluir jogador")
    print("0. Sair")

    opcao = input("\nOpção: ").strip()

    match opcao:
        case "1":
            while True:
                nome = input("Nome: ").strip()
                if nome != "":
                    break
                else:
                    print("Erro: O nome não pode ficar em branco.")

            while True:
                posicao = input("Posição: ").strip()
                if posicao != "":
                    break
                else:
                    print("Erro: A posição não pode ficar em branco.")

            while True:
                camisa_input = input("Camisa: ").strip()
                if camisa_input.isdigit() and int(camisa_input) > 0:
                    camisa = int(camisa_input)

                    # Verifica duplicidade
                    duplicada = False
                    for jogador in elenco:
                        if jogador["camisa"] == camisa:
                            duplicada = True
                            break

                    if duplicada:
                        print(f"Erro: A camisa #{camisa} já está em uso por outro jogador!")
                    else:
                        break
                else:
                    print("Erro: A camisa deve ser um número inteiro positivo.")

            elenco.append({"nome": nome, "posicao": posicao, "camisa": camisa})
            print("Jogador cadastrado!")

        case "2":

            if len(elenco) == 0:
                print("\nO elenco está vazio.")
            else:
                print()
                for idx, jogador in enumerate(elenco, start=1):
                    print(f"{idx}. {jogador['nome']} | {jogador['posicao']} | #{jogador['camisa']}")

        case "3":

            if len(elenco) == 0:
                print("\nO elenco está vazio.")
            else:
                print()
                for idx, jogador in enumerate(elenco, start=1):
                    print(f"{idx}. {jogador['nome']} | {jogador['posicao']} | #{jogador['camisa']}")

                num_input = input("\nDigite o número do jogador para atualizar: ").strip()
                if num_input.isdigit() and 1 <= int(num_input) <= len(elenco):
                    idx_atualizar = int(num_input) - 1

                    while True:
                        nome = input("Novo Nome: ").strip()
                        if nome != "":
                            break
                        else:
                            print("Erro: O nome não pode ficar em branco.")

                    while True:
                        posicao = input("Nova Posição: ").strip()
                        if posicao != "":
                            break
                        else:
                            print("Erro: A posição não pode ficar em branco.")

                    while True:
                        camisa_input = input("Nova Camisa: ").strip()
                        if camisa_input.isdigit() and int(camisa_input) > 0:
                            camisa = int(camisa_input)


                            duplicada = False
                            for i, jogador in enumerate(elenco):
                                if jogador["camisa"] == camisa and i != idx_atualizar:
                                    duplicada = True
                                    break

                            if duplicada:
                                print(f"Erro: A camisa #{camisa} já está em uso por outro jogador!")
                            else:
                                break
                        else:
                            print("Erro: A camisa deve ser um número inteiro positivo.")

                    elenco[idx_atualizar] = {"nome": nome, "posicao": posicao, "camisa": camisa}
                    print("Jogador atualizado!")
                else:
                    print("Erro: Número inválido.")

        case "4":
            if len(elenco) == 0:
                print("\nO elenco está vazio.")
            else:
                print()
                for idx, jogador in enumerate(elenco, start=1):
                    print(f"{idx}. {jogador['nome']} | {jogador['posicao']} | #{jogador['camisa']}")

                num_input = input("\nDigite o número do jogador para excluir: ").strip()
                if num_input.isdigit() and 1 <= int(num_input) <= len(elenco):
                    removido = elenco.pop(int(num_input) - 1)
                    print(f"Jogador '{removido['nome']}' removido!")
                else:
                    print("Erro: Número inválido.")

        case "0":
            print("Saindo...")
            break

        case _:
            print("Erro: Opção inválida!")