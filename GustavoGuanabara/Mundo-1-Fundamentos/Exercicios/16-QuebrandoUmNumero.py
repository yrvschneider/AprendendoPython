# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 o número 6.127 tem a parte inteira 6

import math

n = float(input('Número Real: '))

print('''
Número Real: {}
Portção Inteira: {}
'''.format(n, math.floor(n)))