# Faça um programa que leia um angulo qualquer e mostre na tela
#  o valor do seno, cosseno e tangente desse angulo.

import math

a = float(input('Valor de um Angulo: '))

s = math.sin(a)
c = math.cos(a)
t = math.tan(a)

print('''
Angulo = {}
Seno = {}
Cosseno = {}
Tangente = {}
'''.format(a, s, c, t))