# Escreva um progama que faça o computador "pensar"
#  em um número inteiro entre 0 e 5 e peça para o
#  usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

for i in range(0,3):
    n = int(input('Escolha um número: '))
    pc = random.randrange(0,6)
    if n == pc:
        print('''
        Você acertou!
        Seu número: {}
        Número do PC: {}
        '''.format(n,pc))
        if n == pc:
            break
    else:
        print('''
        Você errou!
        Seu número: {}
        Número do PC: {}
        '''.format(n,pc))