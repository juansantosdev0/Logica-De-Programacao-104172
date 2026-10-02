import os
os.system("cls")


soma = 0
QUANTIDADE_DE_NOTAS = 2

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+i}º nota do aluno: "))
        if nota >= 1 or nota <= 10:
            soma = soma + nota
        break
    else:
        print("Erro na nota, tente novamente!")

    media = soma / QUANTIDADE_DE_NOTAS

print(f"medias, {media} ")
print("=== FIM ===")