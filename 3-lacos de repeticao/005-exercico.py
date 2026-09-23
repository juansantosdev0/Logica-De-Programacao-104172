import os
os.system("cls")

Quantidade_repeticoes = 5
pares = 0
impares = 0

for i in range(Quantidade_repeticoes):
    numero = int(input("Digite um Numero: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")

print("Fim")