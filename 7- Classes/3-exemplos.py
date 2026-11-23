from dataclasses import dataclass
import os

os.system("cls")

# 1. Nome da classe com inicial maiúscula (convenção)
@dataclass
class Cliente:
    nome: str
    telefone: int
    email: str

    # 2. Todos os métodos devem estar indentados (4 espaços) dentro da classe
    def mostrar_dados(self):
        print(f"NOME: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print("=" * 30)

    def zap_marketing(self):
        print(f"NOME: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print("=" * 30)

    def email_marketing(self):
        print(f"NOME: {self.nome}")
        print(f"Email: {self.email}")
        print("=" * 30)


# 3. A lista deve ser criada ANTES do loop de cadastro
listar_clientes = []

print("- Solicitando Dados -")
for i in range(2):
    dados = Cliente(
        nome=input("Digite o seu nome: "),
        telefone=int(input("Digite o Seu Telefone: ")),
        email=input("Digite o Seu E-mail: ")
    )
    listar_clientes.append(dados)

# 4. Exibindo os dados (usando 'item' ou 'c' para não conflitar com 'Cliente')
print("\n= Exibindo Dados =")
for item in listar_clientes:
    item.mostrar_dados()

print("\n= Exibindo Zap Marketing =")
for item in listar_clientes:
    item.zap_marketing()