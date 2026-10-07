import os
os.system("cls")

soma = 0
quantidade = 0

while True:
    valor = int(
        input("Digite um número inteiro positivo : ")
    )

    if valor < 0:
        break

    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"\nA média aritmética dos {quantidade} número(s) é: {media:.2f}")
else:
    print("\nNenhum número positivo foi informado.")