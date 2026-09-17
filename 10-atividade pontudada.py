import os
os.system("cls")

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ")


if tipo == "A" or tipo == "a":
    preco_litro = 3.79

    if litros <= 25:
        desconto = 0.10
    else:
        desconto = 0.20

    
    valor_sem_desconto = litros * preco_litro
    valor_desconto = valor_sem_desconto * desconto
    total = valor_sem_desconto - valor_desconto

    print("Total a pagar: R$", round(total, 2))

elif tipo == "G" or tipo == "g":
    preco_litro = 6.59

    if litros <= 25:
        desconto = 0.15 
    else:
        desconto = 0.30

    
    valor_sem_desconto = litros * preco_litro
    valor_desconto = valor_sem_desconto * desconto
    total = valor_sem_desconto - valor_desconto

    print("Total a pagar: R$", round(total, 2))


else:
    print("Tipo de combustível inválido!")