import os
os.system("cls")

def precos_produto():
    valor = float(input("Digite o preço de um produto: "))
    if valor <= 100:
        valor = valor + (valor * 0.10)
    else:
        valor = valor + (valor * 0.20)
    return  valor


resultado  = precos_produto()

print("\n= EXIBINDO DADOS =")
print(f"O valor é: {resultado:.2f}")