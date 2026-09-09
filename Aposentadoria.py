import os
os.system("cls")

maticula = int(input("Digite sua matricula: "))
idade = int(input("Ano de nascimento: "))
tempo = float(input("Digite seu tempo de trabalho: "))

if  idade >= 65 and tempo >= 30:
    print("Requerer Aposentadoria:")
else:
    print("Não requerer aposentadoria:")
