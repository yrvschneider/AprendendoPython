# Faça um programa que leia o comprimento do cateto oposto
#  e do cateto adjacente de um triangulo, retangulo,
#  calcule e mostre o comprimento da hipotenusa.

from math import hypot

oposto = float(input('Cateto Oposto: '))
adjacente = float(input('Cateto Adjacente: '))

h = hypot(oposto, adjacente)
print('Hipotenusa: {:.2f}'.format(h))