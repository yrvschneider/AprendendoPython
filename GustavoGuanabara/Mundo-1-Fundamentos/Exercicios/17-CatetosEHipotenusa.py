# Faça um programa que leia o comprimento do cateto oposto
#  e do cateto adjacente de um triangulo, retangulo,
#  calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

print('{}'.format(math.hypot(co, ca)))
