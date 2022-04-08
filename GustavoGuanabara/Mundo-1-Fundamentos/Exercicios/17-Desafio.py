# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, retangulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

o = float(input('Digite o valor do Cateto Oposto: '))
a = float(input('Digite o valor do Cateto Adjacente: '))
# h = (o ** a + a ** 2) ** (1/2) # Froma sem utilizar o import
h = hypot(o,a)

print('Cateto Oposto {}, Cateto Adjacente {}, o valor da Hipotenusa é: {:.2f}'.format(o,a,h))