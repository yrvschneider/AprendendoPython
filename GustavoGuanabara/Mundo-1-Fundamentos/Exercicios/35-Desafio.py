# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Comprimento da Primeira Reta: '))
r2 = int(input('Comprimento da Segunda Reta: '))
r3 = int(input('Comprimento da Terceira Reta: '))

if(r2 < r1+r3):
    print('Forma um Triangulo!')
else:
    print('Não forma um Triangulo!')