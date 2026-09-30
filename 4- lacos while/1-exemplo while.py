import os
os.system("cls")

while True:
    numero =  int(input("Digite um numero entre 1 a 10"))
    if numero < 1 or numero > 10:
        print("Numero invalido tente novamente!")
    else:
        print("O numero está entre 1 a 10:")
        break # serve para laços de repetição.

print("= FIM =")