import os
os.system("cls")

vetor_numeros = []


for i in range(5):
    numero = int(input(f"Digite seu {i + 1} Numero: "))
    
    if numero < 0:
        vetor_numeros.append(0.0)
    else:
        vetor_numeros.append(numero)

print("\nValores do vetor:")

for index, numero in enumerate(vetor_numeros, start=1):
    print(f"Posição {index}: {numero}")