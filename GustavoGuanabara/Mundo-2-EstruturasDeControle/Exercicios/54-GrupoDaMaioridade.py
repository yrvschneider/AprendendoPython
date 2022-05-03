# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maior = 0
menor = 0
for i in range(1,8):
    ano = int(input('Digite Ano de nascimento: '))
    idade = date.today().year
    maioridade = idade - ano
    if maioridade >= 18:
        maior += 1
    else:
        menor += 1
print('Maiores de idade {}'.format(maior))
print('Menores de idade {}'.format(menor))