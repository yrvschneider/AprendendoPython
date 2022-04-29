# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# ano = int(input('Digite um ano para ver se ele é Bissexto: '))

# if(0 == ano%4 and 0 == ano%100 and 0 == ano%400):
#     print('Ano Bissexto')
# else:
#     print('Não é ano Bissexto')

# Formula do Professor

from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year # Este comando ira pegar o ano atual da maquina

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))