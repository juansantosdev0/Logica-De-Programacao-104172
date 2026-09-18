import os
os.system("cls")

kg_morango = float(input("Digite a quantidade de morangos (Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (Kg): "))

preco_morango = kg_morango * 2.50 if kg_morango <= 5 else kg_morango * 2.20
preco_maca = kg_maca * 1.80 if kg_maca <= 5 else kg_maca * 1.50

total_kg = kg_morango + kg_maca
total_preco = preco_morango + preco_maca

if total_kg >= 10 or total_preco > 15.00:
    total_preco *= 0.90

print(f"Valor a ser pago: R$ {total_preco:.2f}")