import os
os.system

A = float(input("Digite A: "))
B = float(input("Digite B:"))
C = float(input("Digite C: "))
soma = A + B

if soma > C:
    print("Maior que C: ")
elif soma < C:
    print("Menor que C: ")
else:
    print("Igual a C: ")


