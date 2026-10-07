import os
os.system("cls")




QUANTIDADE_DE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota do aluno: "))
        
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break
        else:
            print("Erro na nota, tente novamente!")

media = soma / QUANTIDADE_DE_NOTAS

print(f"\nMédia: {media:.2f}")

if media >= 7.0:
    print("Situação: Aprovado")
elif media >= 5.0:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")

print("====FIM====")