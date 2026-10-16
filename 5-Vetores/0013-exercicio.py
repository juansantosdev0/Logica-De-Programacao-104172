
pratos = ["Picanha", "Lasanha", "Strogonoff", "Bife Acebolado", "Pão com ovo"]
precos = [25.00, 20.00, 18.00, 15.00, 5.00]


pedidos_pratos = []
pedidos_precos = []

total_conta = 0.0

while True:
    print("\n=== CARDÁPIO ===")

    for i in range(len(pratos)):
        print(f"{i + 1} - {pratos[i]} : R$ {precos[i]:.2f}")

    opcao = int(input("\nDigite o código do prato desejado (1 a 5): "))


    match opcao:
        case 1 | 2 | 3 | 4 | 5:
            indice = opcao - 1
            
            pedidos_pratos.append(pratos[indice])
            pedidos_precos.append(precos[indice])
            
            total_conta += precos[indice]
            print(f"-> {pratos[indice]} adicionado com sucesso!")
        case _:
            print("Código inválido! Tente novamente.")
            continue

    resposta = input("\nDeseja escolher outro prato? (s/n): ").strip().lower()
    if resposta != 's':
        break

print("\n=== RESUMO DA CONTA ===")
for i in range(len(pedidos_pratos)):
    print(f"- {pedidos_pratos[i]}: R$ {pedidos_precos[i]:.2f}")

print(f"\nVALOR TOTAL DA CONTA: R$ {total_conta:.2f}")