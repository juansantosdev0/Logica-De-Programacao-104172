import os
os.system("cls")

print("==== Menu de opções =====")
print("1 - Placa de video: R$ 5000.00")
print("2 - Placa mae : R$ 650.50")
print("3 - Memoria ram: R$ 700.00")
print("4 - Ssd nvme: R$ 560.50")
print("5 - Gabinete: R 300.00")
print("=========================")

while True:
    Componentes = input("Digite o Produto necessario visto pelo numero de identificação: ")

    match Componentes:
        case "1":
            print("\nPlaca de video R$ 5000.00")
            break
        case "2":
            print("\nPlaca mae R$ 650.50")
            break
        case "3":
            print("\nMemoria ram  R$ 700.00")
            break
        case "4":
            print("\nSsd Nvme R$ 560.00")
            break
        case "5":
            print("\nGabinete R$ 300.00")
            break
        case _:
            input("\nErro, Pressione uma tecla se deseja voltar para confimar o numero correto...")
