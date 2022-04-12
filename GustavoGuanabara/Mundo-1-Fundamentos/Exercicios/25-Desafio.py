# Crie um programa que leia um nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite seu nome completo: ')

n1 = nome.lower()
n2 = 'silva' in n1

if(n2 == True):
    print('Nome mencionado tem Silva')
else:
    print('Nome mencionado não tem Silva')