import os
os.system("cls")

# 1. Entrada de dados
renda = float(input("Digite a renda mensal (R$): "))
emprestimo = float(input("Digite o valor do empréstimo (R$): "))
parcelas = int(input("Digite o número de prestações: "))

# 2. Cálculos das regras
valor_parcela = emprestimo / parcelas
limite_emprestimo = renda * 10
limite_parcela = renda * 0.30

# 3. Verificação dos critérios
emprestimo_ok = emprestimo <= limite_emprestimo
parcela_ok = valor_parcela <= limite_parcela

# 4. Exibição do resultado
print("\n--- Resultado da Análise ---")
if emprestimo_ok and parcela_ok:
    print("Empréstimo CONCEDIDO!")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
else:
    print("Empréstimo NEGADO.")
    if not emprestimo_ok:
        print(f"- O valor solicitado ultrapassa o limite de R$ {limite_emprestimo:.2f} (10x a renda).")
    if not parcela_ok:
        print(f"- A parcela (R$ {valor_parcela:.2f}) ultrapassa o limite de R$ {limite_parcela:.2f} (30% da renda).")