from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class Cliente:
    nome: str
    telefone: int
    email: str

    def mostrar_dados(self):
        print(f"NOME: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print("=" * 30)

listar_clientes = []

print("- Solicitando Dados -")
for i in range(2):
    dados = Cliente(
        nome=input("Digite o seu nome: "),
        telefone=int(input("Digite o Seu Telefone: ")),
        email=input("Digite o Seu E-mail: ")
    )
    listar_clientes.append(dados)

print("\n= Exibindo Dados =")
for cliente in listar_clientes:
    cliente.mostrar_dados()