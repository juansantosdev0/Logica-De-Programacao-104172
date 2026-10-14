import os
os.system("cls")

numeros = []
pares = 0
impares = 0

for i in range(6):
    numero = int(input(f"Digite seu {i+1} Numero: "))
    numeros.append(numero)


    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nNúmeros informados: {numeros}")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
saasa