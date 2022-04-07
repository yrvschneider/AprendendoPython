# Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos Dolares ela pode comprar.
#Considere US$ 1,00 = R$ 3,27

carteira = float(input('Quanto de dinehrio você tem na carteira? '))
conversao = carteira / 3.27
print('Você pode comprar US$ {:.2f} Dolares, com o valor que tem na carteira'.format(conversao))