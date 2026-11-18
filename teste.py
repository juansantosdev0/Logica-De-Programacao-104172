def cadastro():
    Matricula_cadastrada = "trabalhador01"
# ==============================================================================
def calcular_inss(salario_base):
    if salario_base <= 1518.00:
        return salario_base * 0.075
    elif salario_base <= 2793.88:
        return (1518.00 * 0.075) + ((salario_base - 1518.00) * 0.09)
    elif salario_base <= 4190.83:
        return (1518.00 * 0.075) + ((2793.88 - 1518.00) * 0.09) + ((salario_base - 2793.88) * 0.12)
    elif salario_base <= 8157.41:
        return (1518.00 * 0.075) + ((2793.88 - 1518.00) * 0.09) + ((4190.83 - 2793.88) * 0.12) + ((salario_base - 4190.83) * 0.14)
    else:
        return 951.62