# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ele não pode esceder 30% do salário ou então o empréstimo será negado.

salario = float(input('Seu Salario: R$'))
casa = float(input('valor da Casa: R$'))
anos = int(input('Quantos anos quer pagar a Casa? '))

trinta = salario * (30/100)
parcelas = 12 * anos
valorParcela = casa / parcelas

if valorParcela <= trinta:
    print('Emprestimo Aprovada!')
    print('Parcelas de R${:.2f} em {} meses.'.format(valorParcela,parcelas))
else:
    print('Emprestimo Negado!')