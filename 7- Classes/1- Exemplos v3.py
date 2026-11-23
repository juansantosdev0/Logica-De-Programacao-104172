from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    nome: str
    idade: int

lista_clientes = []

lista_clientes.append(cliente(nome= "Marta", idade= 30))
lista_clientes.append(cliente(nome= "José", idade= 40))

cliente1 = cliente("Marta", 30)
cliente2 = cliente("José", 40)


for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print("="*15)