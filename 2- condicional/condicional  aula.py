import os
os.system("cls")


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

media = (numero1 + numero2) / 2
print("A média dos números é: ", media)
soma = numero1 + numero2
print("A soma dos números é: ", soma)
produto = numero1 * numero2
print("O produto dos números é: ", produto)

if numero1 > numero2:
    print("O maior número é: ", numero1)
if numero2 < numero1:
    print("O menor número é: ", numero2)
else:
    print("Os números são iguais")
