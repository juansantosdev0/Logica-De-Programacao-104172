import os
os.system("cls")

def exibir_tabuada(numero):
    print(f"--- Tabuada do {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicita a entrada do número ao utilizador
num = int(input("Introduza um número: "))

# Chama a função para exibir o resultado
exibir_tabuada(num)