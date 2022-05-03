# Faça um programa que leia um número inteiro 
# e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))

if n // 2 == 1:
    print('É um número primo!')
else:
    print('Não é um número primo!')