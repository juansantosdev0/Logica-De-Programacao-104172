from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class cliente:
    nome: str
    idade: int
    altura: float

Quantidade_clientes = 2
lista_clientes = []

for i in range(Quantidade_clientes):
    novo_cliente = cliente(
        nome = input("DIGITE SEU NOME: "),
        idade = int(input("DIGITE SUA IDADE: ")),
        altura = float(input("DIGITE SUA ALTURA: "))
    )
    lista_clientes.append(novo_cliente)

arquivo = "dados_cliente.csv"
with open(arquivo, "a") as arquivo_clientes:
    for cliente in lista_clientes:
        arquivo_clientes.write(f"{cliente.nome}, {cliente.idade}, {cliente.altura}\n")

print("Cliente salvo com sucesso!\n")