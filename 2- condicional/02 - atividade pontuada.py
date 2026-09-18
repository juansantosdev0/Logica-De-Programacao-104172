import os
os.system("cls")

nome = input("Digite seu Nome: ")
sexo = input("Digite seu Sexo (M/F): ").strip().upper()
estado_civil = input("Digite seu estado civil: ").strip().upper()

tempo_casada = None

match (sexo, estado_civil):
    case ("F", "CASADA"):
        tempo_casada = int(input("Digite o tempo de casada (em anos): "))
    case _:
        pass

# Exibição dos dados ao final
print("\n--- Dados do Usuário ---")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

if tempo_casada is not None:
    print(f"Tempo de casada: {tempo_casada} anos")