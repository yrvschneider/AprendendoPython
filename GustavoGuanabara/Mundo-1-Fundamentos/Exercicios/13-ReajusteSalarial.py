# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salario atual: R$'))

aumento = salario+(salario*(15/100))

print('''
Seu salario antigo é R${:.2f}
Seu novo salario R${:.2f}
Teve um aumento de 15%, equivalente a R${:.2f}
'''.format(salario,aumento,aumento-salario))