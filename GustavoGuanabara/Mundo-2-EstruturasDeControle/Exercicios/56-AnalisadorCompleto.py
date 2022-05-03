# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

soma = 0
mais = 0
nomeMais = ''
mulher = 0
for i in range(0, 4):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).lower()

    soma = soma + idade
    if mais <  idade:
        mais = idade
        nomeMais = nome
    if 'mulher' == sexo and idade < 20:
        mulher += 1

media = int(soma / 4)

print('''
    Idade media: {} anos
    Homem mais velho: {}
    Quantas mulheres abaixo de 20 anos {}
    '''.format(media, nomeMais, mulher))
