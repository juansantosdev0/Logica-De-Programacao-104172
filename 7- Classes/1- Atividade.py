from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print(f"NOME: {self.nome}")
        print(f"IDADE: {self.idade}")
        print(f"TELEFONE: {self.telefone}")
        print(f"ENDEREÇO: {self.endereco}")
        print()

    def mostrar_nome_idade(self):
        print(f"NOME: {self.nome}")
        print(f"IDADE: {self.idade}")
        print()

    def mostrar_nome_telefone(self):
        print(f"NOME: {self.nome}")
        print(f"TELEFONE: {self.telefone}")
        print()

lista_pacientes = []

print("Solicitando dados do paciente")
for i in range(1):
    dados_do_paciente = Paciente(
        nome=input("Digite o seu nome: "),
        idade=int(input("Digite a sua idade: ")),
        telefone=input("Digite o seu telefone: "),
        endereco=input("Digite o seu endereço: ")
    )
    lista_pacientes.append(dados_do_paciente)
    print()

print("\n= Exibindo todos os dados =")
for item in lista_pacientes:
    item.mostrar_dados()

print("\n= Exibindo nome e idade =")
for item in lista_pacientes:
    item.mostrar_nome_idade()

print("\n= Exibindo nome e telefone =")
for item in lista_pacientes:
    item.mostrar_nome_telefone()