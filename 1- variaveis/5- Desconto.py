import os

#limpa terminal
os.system('cls')

print(' = solicitando dados = ')
valor = float(input('digite o valor: '))

#Calculando
#Desconto 10%
desconto = valor * 0.10
valor_com_desconto = valor - desconto


print('\n= Exibindo Dados =')
print('valor com desconto de 10%: ', valor_com_desconto)