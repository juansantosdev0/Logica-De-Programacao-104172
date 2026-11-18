import os
os.system("cls")

def cadastro():
    Matricula_cadastrada = "trabalhador01"
    Senha_cadastrada = "clt00"
    tentativas = 0

    while tentativas < 3:
        matricula = input("Digite sua Matricula: ").strip()
        senha = input("Digite sua Senha: ").strip()

        if matricula == Matricula_cadastrada and senha == Senha_cadastrada:
            print("\n=Acesso Liberado =")
            return matricula
        else:
            tentativas += 1
            print(f"Dados inválidos! Tentativa {tentativas} de 3.\n")

def calcular_inss(salario_base):
    if salario_base <= 1621.00:
        return salario_base * 0.075
    elif salario_base <= 2902.85:
        return (1621.00 * 0.075) + ((salario_base - 1621.00) * 0.09)
    elif salario_base <= 4354.28:
        return (1621.00 * 0.075) + ((2902.85 - 1621.00) * 0.09) + ((salario_base - 2902.85) * 0.12)
    elif salario_base <= 8475.55:
        return (1621.00 * 0.075) + ((2902.85 - 1621.00) * 0.09) + ((4354.28 - 2902.85) * 0.12) + ((salario_base - 4354.28) * 0.14)
    else:
        return 988.10

matricula = cadastro()

if matricula is not None:
    salario_base = float(input("Digite seu salario: "))
    while salario_base <= 0:
        print("Erro: o salário deve ser maior que zero.")
        salario_base = float(input("Digite seu salario: "))

    inss = calcular_inss(salario_base)
    print(f"INSS: R$ {inss:.2f}")