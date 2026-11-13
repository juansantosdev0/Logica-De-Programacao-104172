import os
os.system("cls")

def numeros_pares_ou_impares(numero):
    if numero % 2 == 0:
        resultado = "Pares"
    else:
        resultado = "Impares"
    return resultado

numero = int(input("Digite um numero: "))


resultado = numeros_pares_ou_impares(numero)

print("= EXIBINDO DADOS =")
print(f" O Numero É: {numero} é {resultado} ")
