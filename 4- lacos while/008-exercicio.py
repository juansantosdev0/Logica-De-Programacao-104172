import os
os.system("cls")

print("====CADASTRO====")
while True:
    login = input("Crie seu login: ")
    senha = input("Crie sua senha: ")
    break

print("======LOGIN=====")
while True:
    login_salvo = input("Coloque seu login: ")
    senha_salva = input("Coloque sua senha: ")
    if login == login_salvo and senha == senha_salva:
        print("Acesso validade, Seja Bem-Vindo")
        break
    else:
        print("\nLogin ou senha incorreto, tente novamente")
        input("pressione qualquer tecla para continuar...")


print("===Fim===")
