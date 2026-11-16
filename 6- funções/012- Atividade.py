import os
import time
os.system("cls")


def ano_nascimento():
    ano = int(input("Digite o seu Ano de Nascimento: "))
    idade = time.localtime().tm_year - ano
    return idade


print(f"Sua idade é : {ano_nascimento()}")


