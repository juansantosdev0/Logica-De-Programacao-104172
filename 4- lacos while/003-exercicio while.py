import os
os.system("cls")
soma = 0
QUANTIDADE_DE_NOTAS = 2

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota1 = float(input(f"Digite A {i+i} nota do aluno: "))
        if nota1 >= 0 and nota1 <= 10:
                soma = soma + nota1
        break
    else:
        print("Nota invalida tente novamente! ")
media = soma / QUANTIDADE_DE_NOTAS

print(f"media: {media}")
print("= FIM =")
