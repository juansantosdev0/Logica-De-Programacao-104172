import os
os.system("cls")

def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) /2
    return resultado

print("= SOLICITANDO NOTAS =")
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = calcular_notas(nota1, nota2)

print("\n= EXIBINDO NOTAS")
print(f"Media {media}")
