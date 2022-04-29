# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrado.

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

tinta = (largura * altura)/2

print('Você ira precisa de {} litros de tinta para printar esta parede.'.format(tinta))