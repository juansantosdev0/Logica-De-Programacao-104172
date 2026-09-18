import os
os.system("cls")

codigo = int(input("digite um prato:"))

match codigo:

    case 1:
        print("prato: Picanha / Valor: R$ 25,00")
    case 2:
        print("prato: Lasanha / Valor: R$ 25,00")
    case 3:
        print("prato: Strogonoff / Valor R$ 18,00")
    case 4:
        print("prato: Bife acebolado / Valor R$ 15,00")
    case 5:
        print("prato: Pão com ovo / Valor R$ 5,00")
