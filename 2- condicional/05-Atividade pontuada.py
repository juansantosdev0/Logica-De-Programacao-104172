import os
os.system("cls")

operacao = input("Digite a operação (+, -, *, /): ").strip()
A = int(input("Digite o numero inteiro (A): "))
B = int(input("Digite o numero inteiro (B): "))

if operacao == "+":
    resultado = A + B
    print(f"resultado {A} + {B} = {resultado}")
elif operacao == "-":
    resultado = A - B
    print(f"resultado {A} - {B} = {resultado}")
elif operacao == "*":
    resultado = A * B
    print(f"resultado {A} * {B} = {resultado}")
elif operacao == "/":
    resultado = A / B
    print(f"resultado {A} / {B} = {resultado}")
else:
    print("Erro: Divisão por zero não é permitida.")