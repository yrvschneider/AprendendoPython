# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Número: '))
print('''
    Número {}
    Sucessor {}
    Antecessor {}
    '''.format(n, n+1, n-1))