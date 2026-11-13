import os
os.system("cls")

def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) /2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    return resultado

print("= SOLICITANDO  DADOS")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = calcular_notas(nota1, nota2)
situacao = verificar_resultado(media)


print("\n= EXIBINDO NOTAS")
print(f"Media: {media}")
print(F"Resultado: {situacao}")