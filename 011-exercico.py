import os
os.system("cls")

nota = 0
soma = 0.0
media = 0

for i in range (1,4):
    nota = float(input(f"Digite a {i}º nota: "))

    soma += nota
    media = soma / 3

if media >= 7:
    print("aprovado: ")
    print(f"media:{media}")
elif media >= 4:
    print("recuperação: ")
    print(f"media:{media}")
else:
    print("reprovado:")
    print(f"media:{media}")



