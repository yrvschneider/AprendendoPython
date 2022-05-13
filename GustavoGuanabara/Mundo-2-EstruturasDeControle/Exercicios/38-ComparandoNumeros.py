# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é MAIOR
# O segundo valor é MAIOR
# Não existe valor maior, os dois São igauis

n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))

if n1 > n2:
    print('O Primeiro Número é MAIOR!')
elif n2 > n1:
    print('Segundo Número é MAIOR!')
elif n1 == n2:
    print('Ambos Números IGUAIS!')