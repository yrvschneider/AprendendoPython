# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL  e CONSIÇÃO DE PAGAMENTGO:

# À vista dinheiro: 10% de desconto
# À vista no cartão: 5% de desconsto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

from math import prod


produto = float(input('Preço do produto: R$'))

opcao = int(input('''
[1] - À Vista Dinheiro - Desconto de 10%
[2] - À Vista Debito - Desconto de 5%
[3] - 2x Credito - Sem desconto
[4] - 3x ou mais no Credito - Acrescimo 20%
'''))

if opcao == 1:
    preco = produto-(produto*(10/100))
    print('Valor a pagar R${:.2f}'.format(preco))
elif opcao == 2:
    preco = produto-(produto*(5/100))
    print('Valor a pagar R${:.2f}.'.format(preco))
elif opcao == 3:
    print('Valor a pagar R${:.2f}.'.format(produto))
elif opcao == 4:
    preco = produto+(produto*(20/100))
    parcelas = int(input('Quantas vezes deseja fazer? '))
    valor = preco / parcelas
    print('Valor a pagar R${:.2f}, será pago em {}x de R${:.2f}.'.format(preco,parcelas,valor))