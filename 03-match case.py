import os
os.system("cls")

numero1 = float(input("Escolha o primeiro numero: "))
# 1. Faltava ler o operador:
operador = input("Escolha a operacao (+, -, *, /): ")
numero2 = float(input("Escolha o segundo numero: "))

# 2. Blocos case preenchidos e formatados:
match operador:
    case "+":
        resultado = numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")
    case "-":
        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")
    case "*":
        resultado = numero1 * numero2
        print(f"{numero1} * {numero2} = {resultado}")
    case "/":
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")