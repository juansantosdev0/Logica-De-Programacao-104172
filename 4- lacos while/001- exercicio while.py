import os
os.system("cls")

while True:
    numero = int(input("Digite a nota do aluno entre 0 e 10: "))
    if numero < 0 or numero > 10:
        print() # pular uma linha
        print("Numero invalido tente novamente")
    else:
        print() # Assim como o \n
        print("Sua nota é", numero)
        break # serve para laços de repetição.

print("= FIM =")