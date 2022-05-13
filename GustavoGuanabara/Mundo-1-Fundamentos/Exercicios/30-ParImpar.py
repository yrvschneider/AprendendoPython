# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

n = int(input('Número: '))

par = n % 2

if par == 0:
    print('PAR')
else:
    print('IMPAR')