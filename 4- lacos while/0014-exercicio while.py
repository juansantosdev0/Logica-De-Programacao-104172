import os
os.system("cls")

soma_salario = 0
soma_filhos = 0
total_familias = 0
maior_salario = 0
menor_salario = 0

while True:
    print("Código | Descrição")
    print("  1    | Adicionar família")
    print("  2    | Sair e exibir resultados")
    opcao = input("Opção: ")

    os.system("cls")

    if opcao == "1":
        salario = float(input("Salário: R$ "))
        filhos = int(input("Número de filhos: "))

        soma_salario += salario
        soma_filhos += filhos
        total_familias += 1

        if total_familias == 1:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario
            if salario < menor_salario:
                menor_salario = salario

        os.system("cls")
        print("Família adicionada!\n")

    elif opcao == "2":
        if total_familias == 0:
            print("Nenhuma família foi registada.")
        else:
            print(f"a) Total de famílias: {total_familias}")
            print(f"b) Média do salário: R$ {soma_salario / total_familias:.2f}")
            print(f"c) Média do número de filhos: {soma_filhos / total_familias:.1f}")
            print(f"d) Maior salário: R$ {maior_salario:.2f}")
            print(f"e) Menor salário: R$ {menor_salario:.2f}")
        break