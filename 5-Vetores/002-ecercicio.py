import os
os.system("cls")

notas = []

for i in range(3):
    nota = float(input("Digite Sua nota: "))
    notas.append(nota)


medias = sum(notas) / len(notas)
print(f'Media: {medias:.1f}')