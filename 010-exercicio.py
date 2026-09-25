import os
os.system("cls")

media = 0
nota = 0


for i in range(1,5):
    notai = int(input(f"Digite sua nota {i}º: "))
    nota = nota + notai
    media = nota /4


print(f"media:{media}")