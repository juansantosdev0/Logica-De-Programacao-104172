import os
os.system("cls")

dia = input("Digite o dia da semana:")

match dia:

    case "segunda":
        print("Hoje e segunda feira:")
    case "terça":
        print("Hoje e terça-feira:")
    case "quarta":
        print("Hoje e  quarta-feira:")
    case "quinta":
        print("Hoje e quinta feira:")
    case "sexta":
        print("Hoje e sexta-feira:")
    case "sabado":
        print("Hoje e final de semana:")
    case "domingo":
        print("Hoje e final de semana:")
    case _:
        print("Dia invalido:")

print(dia)
print("===FIM===")