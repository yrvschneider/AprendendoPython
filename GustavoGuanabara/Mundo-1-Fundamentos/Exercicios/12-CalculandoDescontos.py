# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual é o preço do produto? R$'))

desconto = produto - ((5 * produto)/100)

print('Produto com desconto de 5%, sai por: R${:.2f}'.format(desconto))