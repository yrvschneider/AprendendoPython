# Crie um programa que faça o computador jogar jokempô com você.

import random

print('Escolha um das opções abaixo.')
print('1 para Desoura / 2 para Papel / 3 para Pedra')
opcao = int(input('Qual opção? '))

papel = 1
desoura = 2
pedra = 3

computador = random.randrange(1,4)

if opcao == computador:
    print('Empate!')
elif opcao == papel and computador == pedra or opcao == desoura and computador == papel or opcao == pedra and computador == desoura:
    print('Ganhou!')
else:
    print('Perdeu!')
    