
from dataclasses import dataclass
import os

os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: str

quantidade_clientes = 3
listar_cliente = []

for i in range(quantidade_clientes):
    novo_cliente = Cliente(
        nome=input("Digite Seu Nome: "),
        email=input("Digite Seu E-mail: "),
        telefone=input("Digite Seu Telefone: "),
        endereco=input("Digite Seu Endereço: ")
    )
    listar_cliente.append(novo_cliente)

arquivo = "Fornecedor.csv"
with open(arquivo, "a") as arquivo_clientes:
    for cliente in listar_cliente:
        arquivo_clientes.write(f"{cliente.nome},{cliente.email},{cliente.telefone},{cliente.endereco}\n")

arquivo = "Fornecedor.csv"
with open(arquivo, "r") as arquivo_clientes:
    for linha in arquivo_clientes:
        campos = linha.strip().split(",")
        if len(campos) != 4:
            continue
        nome, email, telefone, endereco = campos
        listar_cliente.append(Cliente(
            nome=nome, email=email, telefone=int(telefone), endereco=endereco
        ))



print("\nClientes salvos com sucesso!\n")
print("\nExibindo dados dos clientes: ")
for cliente in listar_cliente:
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print(f"Endereço: {cliente.endereco}")
    print("--------------------------")