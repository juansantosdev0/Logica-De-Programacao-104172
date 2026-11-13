import os
os.system("cls")

def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado


print("= SOLICITANDO NOTAS =")
nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))

soma = calcular_notas(nota1, nota2)

print("= EXIBINDO NOTAS")
print(f"Soma: {soma}")