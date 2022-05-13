# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

cidade = str(input('Digite o nome da tua cidade: ')).lower().split()

if 'santo' == cidade[0]:
    print('Cidade começa com o nome SANTO!')
else:
    print('A cidade não inicia com nome SANTO!')