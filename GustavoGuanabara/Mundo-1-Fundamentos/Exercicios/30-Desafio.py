# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

from unicodedata import numeric

n = int(input('Digite um número: '))
r = n % 2

if(r == 0):
    print('PAR')
else:
    print('IMPAR')