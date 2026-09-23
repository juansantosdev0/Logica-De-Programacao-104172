import os
os.system("cls")

numero1 = 0.0

for i in range(1,6):
    numero = int(input(f"Digite um numeros {i}: "))
    numero1 += numero
print(f"A soma é {numero1}")
