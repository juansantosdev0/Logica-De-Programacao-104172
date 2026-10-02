import os
os.system("cls")




QUANTIDADE_DE_NOTAS = 3
soma = 0

# Laço para leitura e validação das 3 notas
for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota do aluno: "))
        
        # Aceita notas de 0 a 10
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break
        else:
            print("Erro na nota, tente novamente!")

# Cálculo da média
media = soma / QUANTIDADE_DE_NOTAS

print(f"\nMédia: {media:.2f}")

# Verificação da situação do aluno
if media >= 7.0:
    print("Situação: Aprovado")
elif media >= 5.0:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")

print("====FIM====")