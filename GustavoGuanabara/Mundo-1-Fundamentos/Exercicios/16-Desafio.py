# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 o número 6.127 tem a parte inteira 6

from math import trunc

n = float(input('Digite um numero real: '))

print('Parte Inteira do número digitado: {}'.format(trunc(n)))