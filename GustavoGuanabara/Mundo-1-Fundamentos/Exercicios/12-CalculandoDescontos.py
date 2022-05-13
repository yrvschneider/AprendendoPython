# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Preço: R$'))

desconto = preco-(preco*(5/100))
print('Novo preço com desconto R${:.2f}'.format(desconto))