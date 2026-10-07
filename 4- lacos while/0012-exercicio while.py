import os
os.system("cls")


qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0

while True:
    numero = int(input("Digite um número inteiro positivo: "))
    

    if numero == 0:
        break
    

    if numero < 0:
        print("Por favor, digite apenas números positivos.")
        continue

    soma_geral += numero
    
    if numero % 2 == 0:
        qtd_pares += 1
        soma_pares += numero
    else:
        qtd_impares += 1


qtd_total = qtd_pares + qtd_impares

print("\n--- Resultados ---")
print(f"a. Quantidade de números pares: {qtd_pares}")
print(f"   Quantidade de números ímpares: {qtd_impares}")


if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f"b. Média de valores pares: {media_pares:.2f}")
else:
    print("b. Média de valores pares: Nenhum número par foi informado.")

if qtd_total > 0:
    media_geral = soma_geral / qtd_total
    print(f"c. Média geral dos números lidos: {media_geral:.2f}")
else:
    print("c. Média geral dos números lidos: Nenhum número válido foi informado.")