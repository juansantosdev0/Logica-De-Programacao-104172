import os 
os.system("cls")

nomes = []

for i in range(4):
    nome = input(f"digite o {i+1}º nome: ")
    nomes.append(nome)

for i in range(4):
    print(f"{i+1}º nome: {nomes[i]}")