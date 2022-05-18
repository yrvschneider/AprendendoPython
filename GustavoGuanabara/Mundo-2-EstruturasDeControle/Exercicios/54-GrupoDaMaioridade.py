# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

meiorIdade = 0
menorIdade = 0

for i in range(1,8):
    entrada = int(input('Ano de Nascimento: '))
    idade = date.today().year - entrada

    if idade <= 18:
        meiorIdade += 1
    else:
        menorIdade += 1

print('''
    Temos {} pessoas com mais de 18 anos.
    Temos {} pessoas menores de 18 anos.
'''.format(meiorIdade, menorIdade))