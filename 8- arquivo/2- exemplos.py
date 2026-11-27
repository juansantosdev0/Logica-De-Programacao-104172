import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    idade: int
    altura: float

QUANTIDADE_CLIENTES = 2

lista_clientes = []

arquivo = "dados_cliente.csv"
with open(arquivo, "r") as arquivo_clientes:
    for linha in arquivo_clientes:
        nome, idade, altura = linha.strip().split(",")
        lista_clientes.append(Cliente(
            nome=nome, idade=int(idade), altura=float(altura)
        ))

print("\nExibindo dados dos clientes: ")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"Altura: {cliente.altura}")
    print("--------------------------")