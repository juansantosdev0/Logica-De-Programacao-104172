import os

os.system("cls")

pacientes = []

while True:
    print('''
1. Cadastrar paciente
2. Listar pacientes
3. Atualizar paciente
4. Excluir paciente
5. Buscar paciente
0. Sair
''')

    opcao = input("Escolha uma Opção: ").strip()

    match opcao:
        case "1":
            print("\nCadastrar Paciente")
            nome = input("Insira o nome do paciente: ").strip()
            sobrenome = input("Digite o sobrenome do paciente: ").strip()

            if nome != "" and sobrenome != "":
                pacientes.append({"nome": nome, "sobrenome": sobrenome})
                print("Paciente cadastrado!")
            else:
                print("Nome e sobrenome não podem ficar em branco!")

        case "2":
            print("\nListar Pacientes")
            if len(pacientes) == 0:
                print("Nenhum paciente cadastrado.")
            else:
                for i in range(len(pacientes)):
                    print(f"{i + 1}. {pacientes[i]['nome']} {pacientes[i]['sobrenome']}")

        case "3":
            print("\nAtualizar Paciente")
            if len(pacientes) == 0:
                print("Nenhum paciente cadastrado.")
            else:
                for i in range(len(pacientes)):
                    print(f"{i + 1}. {pacientes[i]['nome']} {pacientes[i]['sobrenome']}")
                
                pos = int(input("\nDigite o número do paciente para atualizar: ")) - 1
                
                if 0 <= pos < len(pacientes):
                    novo_nome = input("Novo nome: ").strip()
                    novo_sobrenome = input("Novo sobrenome: ").strip()
                    if novo_nome != "" and novo_sobrenome != "":
                        pacientes[pos]["nome"] = novo_nome
                        pacientes[pos]["sobrenome"] = novo_sobrenome
                        print("Paciente atualizado!")
                    else:
                        print("Nome e sobrenome não podem ser vazios!")
                else:
                    print("Número inexistente!")

        case "4":
            print("\nExcluir Paciente")
            if len(pacientes) == 0:
                print("Nenhum paciente cadastrado.")
            else:
                for i in range(len(pacientes)):
                    print(f"{i + 1}. {pacientes[i]['nome']} {pacientes[i]['sobrenome']}")
                
                pos = int(input("\nDigite o número do paciente para excluir: ")) - 1
                
                if 0 <= pos < len(pacientes):
                    removido = pacientes.pop(pos)
                    print(f"Paciente {removido['nome']} {removido['sobrenome']} removido!")
                else:
                    print("Número inexistente!")

        case "5":
            print("\nBuscar Paciente")
            if len(pacientes) == 0:
                print("Nenhum paciente cadastrado.")
            else:
                busca = input("Digite o nome ou sobrenome para buscar: ").strip().lower()
                encontrou = False
                
                for i in range(len(pacientes)):
                    p = pacientes[i]
                    if busca in p["nome"].lower() or busca in p["sobrenome"].lower():
                        print(f"{i + 1}. {p['nome']} {p['sobrenome']}")
                        encontrou = True
                
                if encontrou == False:
                    print("Nenhum paciente encontrado.")

        case "0":
            print("\nA sair do programa...")
            break

        case _:
            print("\nOpção inválida!")