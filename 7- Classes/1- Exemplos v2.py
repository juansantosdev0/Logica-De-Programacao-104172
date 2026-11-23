from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    nome: str
    idade: int

cliente1 = cliente("Marta", 30)


cliente2 = cliente("José", 40)


print(f"Nome:{cliente1.nome}")
print(f"Idade: {cliente1.idade}")

print(f"Nome: {cliente2.nome}")
print(f"Idade: {cliente2.idade}")