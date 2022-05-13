# Crie um programa que leia um nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = 'Leticia carreira da Silva'.lower()

tem = 'silva' in nome

if tem == True:
    print('Este nome tem Silva!')
else:
    print('Este nome não contem Silva!')