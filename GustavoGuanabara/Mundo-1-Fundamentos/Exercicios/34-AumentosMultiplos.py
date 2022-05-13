# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Salario: '))

base = 1250

if salario > base:
    aumento = salario+(salario*(10/100))
    print('''
    Seu salario atual R${:.2f}
    Ira receber 10% de aumento, equivalente a R${:.2f}
    Seu aumento para próximo mês R${:.2f}
    '''.format(salario,aumento-salario,aumento))
elif salario <= base:
    aumento = salario+(salario*(15/100))
    print('''
    Seu salario atual R${:.2f}
    Ira receber 15% de aumento, equivalente a R${:.2f}
    Seu aumento para próximo mês R${:.2f}
    '''.format(salario,aumento-salario,aumento))