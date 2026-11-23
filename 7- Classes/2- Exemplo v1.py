from dataclasses import dataclass
import os
os.system("cls")

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE.
# DADOS: NOME, TELEFONE E E-MAIL.

@dataclass
class cliente:
    nome: str
    telefone: int
    email: str


lista_cliente = []

print("\nSOLICITANDO DADOS DO CLIENTE")
for i in range(1):
    dados_do_cliente = cliente(
        nome= input("Digite o seu nome: "),
        telefone= int(input("Digite o Seu Telefone: ")),
        email= input("Digite o Seu E-mail: ")
)
lista_cliente.append(dados_do_cliente)

print("\nEXIBINDO DADOS DO CLIENTE")
for cliente in lista_cliente:
    print(f"Nome: {cliente.nome}")
    print(f"Telefone: {cliente.telefone}")
    print(F"E-Mail: {cliente.email}")
    print("="*15)
