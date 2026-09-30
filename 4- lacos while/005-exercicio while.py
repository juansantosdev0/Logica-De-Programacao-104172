import os

os.system("cls")

login_salvo = "juan"
senha_salva = "123"
TENTATIVAS = 3

for i in range(1, TENTATIVAS + 1):
    login = input("Digite Seu Login: ")
    senha = input("Digite Sua Senha: ")

    if login == login_salvo and senha == senha_salva:
        print("\nAcesso validado. Seja bem-vindo!")
        break
    else:
        print("\nAcesso negado, tente novamente.")
        if TENTATIVAS < TENTATIVAS:
            input("Pressione uma tecla para poder continuar... ")
        os.system("cls")

print("====== Fim =====")
