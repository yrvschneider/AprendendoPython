# Melhore o jogo do DESAFIO 28 onde o computador vai
#  'pensar' em um número entre 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.

import random

t = 1

while t != 0:
    # n = int(input('Digite um Valor de 0 à 10: '))
    n = random.randrange(1,11)
    pc = random.randrange(1,11)
    t += 1
    if n == pc:
        print('''
        Você acertou!
        Tentativas {}
        Nº Computador {}
        Nº Escolhido {}
        '''.format(t-1, pc, n))
        break
    else:
        print('''
        Você errou!
        Nº Computador {}
        Nº Escolhido {}
        '''.format(pc,n))