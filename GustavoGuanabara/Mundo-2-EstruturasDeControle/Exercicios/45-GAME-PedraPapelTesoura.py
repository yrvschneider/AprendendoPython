# Crie um programa que faça o computador jogar jokempô com você.

import random

escolha = int(input('[1] - Pedra / [2] - Papel / [3] - Tesoura : '))
computador = random.randrange(1,4)

if escolha == computador:
    print('Jogue de novo!')
elif escolha != computador:
    if escolha == 1 and computador == 3 or escolha == 2 and computador == 1 or escolha == 3 and computador == 2:
        print('Você Ganhou!')
        if escolha == 1 and computador == 3:
            print('Pedra vs Tesoura')
        elif escolha == 2 and computador == 1:
            print('Papel vs Pedra')
        elif escolha == 3 and computador == 2:
            print('Tesoura vs Papel')
    else:
        print('Computador Ganhou!')
        if computador == 1 and escolha == 3:
            print('Pedra vs Tesoura')
        elif computador == 2 and escolha == 1:
            print('Papel vs Pedra')
        elif computador == 3 and escolha == 2:
            print('Tesoura vs Papel')