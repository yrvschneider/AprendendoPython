# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaIdade = 0
maisVelho = 0
nomeVelho = ''
mulheres = 0

for i in range(1, 5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[H] Homem e [M] Mulher: ')).upper()
    somaIdade += idade

    if sexo == 'H' and idade > maisVelho:
        nomeVelho = nome
        maisVelho = idade
    elif sexo == 'M' and idade < 20:
        mulheres += 1

media = somaIdade/4

print('''
    Média de idade do grupo: {} anos
    Homem mais velho do grupo: {} com {}
    Mulheres com menos de 20 anos: {} Mulheres
'''.format(media, nomeVelho, maisVelho, mulheres))