import os
os.system("cls")


vetor_numeros = []
numeros_positivos = 0
numeros_negativos = 0

for i in range(5):
    numero = float(input(f"Digite seu {i+1}º Numero: "))
    vetor_numeros.append(numero)

for index, numero in enumerate(vetor_numeros):
    if numero <= 0:
        numeros_negativos += 1
    elif numero >= 0:
        numeros_positivos += 1




print(f"Quantidade de números negativos:{numeros_negativos}")
print(f"Soma dos números positivos: {numeros_positivos}")