import os
os.system("cls") 
media= float(input("digite sua media: "))
faltas = float(input("digite sua faltas: "))

if media <= 7 and faltas >= 48:
    print("aprovado: ")

else:
    print("reprovado: ")