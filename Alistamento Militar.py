import os
os.system("cls")

idade = int(input("digite sua idade"))
sexo = input("digite o sexo (M OU F): ")

if idade >= 18  and sexo == "M":
    resultado = "deve se apresenta-se ao servico militar."
else:
    resultado = "não deve se apresentar ao servico militar."

print(f"resultado {resultado}")