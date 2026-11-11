import os
os.system("cls")

def logo_senai():
    print("\n")
    print("="* 15)
    print("        SENAI")
    print("="* 15)
    


def mostrar_dados(nome, idade, telefone):
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Telefone: {telefone}")

logo_senai()

print("\n= Solicitando Dados =")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = input("Informe seu telefone: ")

print("\n = Exibindo dados =")
mostrar_dados(nome, email, telefone)