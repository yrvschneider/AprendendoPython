# Faça um programa que leia a largura e a altura de uma parede em metros,
#  calcule a sua área e a quantidade de tinta necessária para pintá-la,
#  sabendo que cada litro de tinta, pinta uma área de 2m quadrado.

print('''
Digite a Largura e Altura em Metros de uma parede.
''')
altura = float(input('Altura: '))
largura = float(input('Largura: '))
tinta = float(input('Litros: '))
m2 = int(input('Tinta m²:'))
demao = int(input('Demão: '))

area = largura*altura
litros = area/(m2/demao)

print('''
Sua parede tem Altura {}m e Largura {}m.
Seu metro quadrado é {}m².
A tinta pinta {}m² por {} litro.
Irá precisar de {:.3f} Litros de tinta para pintar a parede com 1 demão.
'''.format(altura,largura,area,m2,tinta,litros))