# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e rais quadrada.

import math


n = int(input('Número: '))
print('''
    Número: {}
    Dobro: {}
    Tripo: {}
    Raiz Quadrada: {:.1f}
'''.format(n,n*2,n*3, math.sqrt(n)))