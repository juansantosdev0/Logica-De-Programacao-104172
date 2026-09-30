import os
os.system("cls")

nome_produto = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    percentual_desconto = 0.02
elif quantidade <= 10:
    percentual_desconto = 0.03
else:
    percentual_desconto = 0.05

valor_desconto = total * percentual_desconto
total_a_pagar = total - valor_desconto

print("\n--- Resumo da Compra ---")
print(f"Produto: {nome_produto}")
print(f"Total bruto: R$ {total:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f} ({int(percentual_desconto * 100)}%)")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")