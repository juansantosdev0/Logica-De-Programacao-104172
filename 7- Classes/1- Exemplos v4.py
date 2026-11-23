from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    nome: str
    idade: int
    altura: float
    peso: float

lista_clientes = []

print("\nSOLICITANDO DADOS DE DOIS CLIENTES")
for i in range(2):
    dados_do_cliente = cliente(
        nome= input("Digite Seu Nome: "),
        idade= int(input("Digite Sua Idade: ")),
        altura= float(input("Digite sua Altura: ")),
        peso= float(input("Digite Seu Peso: "))
    )
    lista_clientes.append(dados_do_cliente)

print("\nEXIBINDO DADOS DOS CLIENTES")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"Altura: {cliente.altura}")
    print(f"Peso: {cliente.peso}")
    print("="*15)