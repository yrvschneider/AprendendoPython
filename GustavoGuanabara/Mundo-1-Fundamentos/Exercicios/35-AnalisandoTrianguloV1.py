# Desenvolva um programa que leia o comprimento de
#  tres retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = int(input('Primeira Reta: '))
n2 = int(input('Segunda Reta: '))
n3 = int(input('Terceira Reta: '))

if n1 < n2 + n3 or n2 < n1 + n3 or n3 < n1 + n2:
    print('Forma um Triangulo!')
else:
    print('Não forma um Triangulo!')