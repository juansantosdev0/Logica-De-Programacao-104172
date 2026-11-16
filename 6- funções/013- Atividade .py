import os

os.system("cls")

def calcular_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)

def mostrar_resultado(listar_notas):
    print("\n= EXIBINDO NOTAS =")
    for nota in lista_notas:
        print(f"Nota: {nota}")
    print(f"\nMedia: {media}")


lista_notas = []

for i in range(3):
    nota = float(input("Digite a sua nota: "))
    lista_notas.append(nota)

media = calcular_media(lista_notas)

print(f"Média: {media:.2f}")

mostrar_resultado(lista_notas)
media = calcular_media(lista_notas)