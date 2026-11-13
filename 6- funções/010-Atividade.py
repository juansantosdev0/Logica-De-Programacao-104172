import os
os.system("cls")

def numeros_calculados():
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um numero: "))
    return n1, n2

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    return n1 / n2

def mutiplicacao(n1, n2):
    return n1 * n2

n1, n2 = numeros_calculados()

print("= EXIBINDO DADOS =")
print(f"Soma: {soma(n1, n2)}")
print(f"Subtração: {subtracao(n1, n2)}")
print(f"Divisão: {divisao(n1, n2)}")
print(f"Mutiplicação: {mutiplicacao(n1, n2)}")
