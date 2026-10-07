import os

os.system("cls")

soma = 0
contador = 0

while True:
    while True:
        nota = float(input(f"Digite a {contador + 1}ª Sua Nota: "))

        if nota >= 0 and nota <= 10:
            soma = soma + nota
            contador = contador + 1
            break
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")

    resposta = input("Deseja inserir mais uma nota? (S/N): ").upper()

    if resposta == "N":
        break

if contador > 0:
    media = soma / contador
    print(f"\nQuantidade de iterações (notas): {contador}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhuma nota foi introduzida.")