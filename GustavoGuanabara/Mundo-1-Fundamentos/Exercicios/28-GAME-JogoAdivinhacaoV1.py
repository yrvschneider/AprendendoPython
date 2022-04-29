# Escreva um progama que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

n1 = int(input('Escolha um número de 0 à 5: '))
n2 = random.randrange(0, 5)

if(n1 == n2):
    print('Número escolhido {}, Número Sorteado {}. Você Ganhou!'.format(n1,n2))
else:
    print('Número escolhido {}, Número Sorteado {}. Você Perdeu!'.format(n1,n2))

# Formula do Professor

# from random import randint
# from time import sleep

# computador = randint(0,5) # Faz o computador pensar 
# jogador = int(input('Em que número eu pensei? '))
# print('PROCESSANDO...')
# sleep(2)

# if jogador == computador:
#     print('PARABENS! Você ganhou!')
# else:
#     print('GANHEI! Eu pensei no número {}'.format(computador))