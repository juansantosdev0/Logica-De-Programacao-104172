import os
os.system("cls")

login_certo = "juan123"
senha_certa = "1234567"

while True:
    login = input("Digite seu login: ")
    senha = int(input("Digite seu password: "))
    if login == login_certo or senha == senha_certa:
        print("Acesso validado, Seja bem-vindo")
        break
    else:
        print("\n Login ou senha incorretos. Tente novamente.")
        input("pressione uma tecla para continuar...")
        os.system("cls")

print("= FIM =")