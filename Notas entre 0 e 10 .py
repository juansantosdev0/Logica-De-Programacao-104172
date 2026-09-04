import os
os.system("cls")

nota = float(input("DIGITE SUA NOTA: "))

if nota >= 0 and nota <= 10:
    print("Correto estar entre o 0 e 10: ")

else:
    print("Nota deve ser entre 0 e 10: ")