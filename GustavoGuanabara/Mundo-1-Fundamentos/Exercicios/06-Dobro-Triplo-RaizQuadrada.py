# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e rais quadrada.

import math

n = int(input('Digite um número: '))

print('''
Entrada: {}
Dobro: {}
Triplo: {}
Raiz Quadrada: {}
'''.format(n, n*2, n*3, math.sqrt(n)))