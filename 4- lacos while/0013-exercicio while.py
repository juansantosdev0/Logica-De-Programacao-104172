import os
os.system("cls")

soma_salario = 0
total_pessoas = 0
maior_idade = 0
menor_idade = 0
mulheres_5k = 0

while True:
    print("1 | Adicionar pessoa")
    print("2 | Exibir resultados")
    print("3 | Sair")
    opcao = input("Opção: ")

    os.system("cls")

    if opcao == "1":
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").upper()
        salario = float(input("Salário: R$ "))

        soma_salario += salario
        total_pessoas += 1

        if total_pessoas == 1:
            maior_idade = idade
            menor_idade = idade
        else:
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade

        if sexo == "F" and salario >= 5000:
            mulheres_5k += 1

        os.system("cls")
        print("Pessoa cadastrada!\n")

    elif opcao == "2":
        if total_pessoas == 0:
            print("Nenhum cadastro realizado.\n")
        else:
            print(f"a) Média salarial: R$ {soma_salario / total_pessoas:.2f}")
            print(f"b) Maior idade: {maior_idade} | Menor idade: {menor_idade}")
            print(f"c) Mulheres com salário >= R$ 5000: {mulheres_5k}\n")

    elif opcao == "3":
        print("-------FIM-------.")
        break