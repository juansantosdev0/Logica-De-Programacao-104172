import os
os.system("cls")

def consultar_preco_cd(cor):
    cor_normalizada = cor.strip().lower()

    match cor_normalizada:
        case "verde":
            preco = 10.00
        case "azul":
            preco = 20.00
        case "amarelo":
            preco = 30.00
        case "vermelho":
            preco = 40.00
        case _:
            print("Cor inválida! Escolha entre Verde, Azul, Amarelo ou Vermelho.")
            return

    print(f"O preço do CD de cor {cor_normalizada.capitalize()} é R$ {preco:.2f}")

cor_input = input("Digite a cor do CD: ")
consultar_preco_cd(cor_input)