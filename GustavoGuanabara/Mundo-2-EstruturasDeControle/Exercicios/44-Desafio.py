# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL  e CONSIÇÃO DE PAGAMENTGO:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconsto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

from math import prod


produto = float(input('Digite o valor do produto: R$'))

print('Qual forma de pagamento?')
print('1 - Dinheiro / 2 - Debito')
print('3 - 2x Credito / 4 - Mais Vezes')
opcao = int(input('Digite a opção escolhida: '))
avista = 1
avistaDebito = 2
prazo2x = 3
prazo = 4

if opcao == avista:
    preco = produto - ((produto*10)/100)
    print('Produto custa R${:.2f} com desconto de 10% ficara R${:.2f}'.format(produto, preco))
elif opcao == avistaDebito:
    preco = produto - ((produto*5)/100)
    print('Produto custa R${:.2f} com desconto de 10% ficara R${:.2f}'.format(produto, preco))
elif opcao == prazo2x:
    print('Valor do produto R${:.2f} no credito em até duas vezes sem juros.'.format(produto))
elif opcao == prazo:
    preco = produto + ((produto*20)/100)
    print('Produto R${:.2f}. Pagamento acima de 3x no credito R${:.2f}'.format(produto,preco))
else:
    print('Opção invalida!')