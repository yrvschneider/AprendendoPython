# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salario do funcionario: R$'))

aumento = salario+((salario*15)/100)

print('Novo salario do funcionario, com aumento de 15% ficara R${:.2f}'.format(aumento))