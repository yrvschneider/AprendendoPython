# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é MAIOR
# O segundo valor é MAIOR
# Não existe valor maior, os dois São igauis

n1 = int(input('Digite o Primeiro valor: '))
n2 = int(input('Digite o Segundo valor: '))

if n1 > n2:
    print('O Primeiro valor é MAIOR {}'.format(n1))
elif n2 > n1:
    print('O Segundo valor é MAIOR {}'.format(n2))
else:
    print('Não existe valor maior, os dois São igauis!')