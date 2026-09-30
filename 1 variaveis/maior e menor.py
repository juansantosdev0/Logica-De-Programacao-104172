import os
os.system
primeiro_numero = int(input( "digite um numero:"))
segundo_numero = int(input("digite um numero:"))
terceiro_numero = int(input("digite um numero:"))

maior_numero = max(primeiro_numero, segundo_numero,terceiro_numero)
menor_numero = min(primeiro_numero,segundo_numero,terceiro_numero)
print("primeiro_numero:", primeiro_numero)
print("segundo_numero:", segundo_numero)
print("terceiro numero:", terceiro_numero)

print("o maior numero é", maior_numero)
print("o menor numero é", menor_numero)
