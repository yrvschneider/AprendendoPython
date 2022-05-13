# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Digite um ano: '))

n1 = ano % 4
n2 = ano % 100
n3 = ano % 400

if n1 == 0 and n2 == 0 or ano == 0:
    print('Ano Bissexto!')
else:
    print('Ano não é Bissexto!')