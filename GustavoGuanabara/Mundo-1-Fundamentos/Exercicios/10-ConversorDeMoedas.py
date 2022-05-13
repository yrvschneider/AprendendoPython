# Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos Dolares ela pode comprar.
#Considere US$ 1,00 = R$ 3,27

print('''
Digite quanto tem de dinheiro na tua carteira''')
carteira = float(input('Valor em real: R$'))

dolar = 3.27
compra = carteira/dolar
troco = carteira-(compra*compra)
print('''
Você tem R${:.2f}, na sua carteira!
Um dolar custa R${}.
Você podera comprar ${:.2f} dolar.
Ira sobrar R${:.2f} na carteira.
'''.format(carteira, dolar, compra, troco))