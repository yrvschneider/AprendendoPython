# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

cidade = str(input('Digite o nome da sua cidade: '))

n = cidade.lower()
n1 = n.split()
n2 = 'santo'[0] in n1[0]

if(n2 == True):
    print('Nome da cidade inicia com SANTO')
else:
    print('Nome da cidade não inicia com SANTO')

# Formato do professor

# cidade = str(input('Digite um nome de uma cidade: ')).strip()
# print(cidade[:5].upper() == 'SANTO')
