import os
os.system("cls")

def verificar_valor(numero):
    if numero >= 1:
        resultado = "Valor Possitivo"
    elif numero == 0:
        resultado = "Valor Neutro"
    else:
        resultado = "Valor Negativo"
    return resultado

numero = int(input("Digite um numero: "))

resultado = verificar_valor(numero)

print("= EXIBINDO DADOS =")
print(f"o Número é: {numero} é {resultado}")