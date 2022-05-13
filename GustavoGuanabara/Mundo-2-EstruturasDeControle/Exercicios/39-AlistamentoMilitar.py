# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade.

# Se ele ainda vai se alsitar ao serviço militar.
# Se é a hora de se alsitar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nome = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))

alistamento = date.today().year - anoNascimento

if alistamento == 18:
    print('É hora de se alistar no serviço militar.')
elif alistamento < 18:
    print('Ainda falta para se alistar no serviço militar.')
    if alistamento == 1:
        print('Falta {} ano para se alistar.'.format(alistamento))
    elif alistamento > 18:
        print('Falta {} anos para se alistar.'.format(alistamento))
elif alistamento > 18:
    print('Já passou da idade de se alistar no serviço militar.')
    if alistamento == 19:
        print('Você passou {} ano do alistamento.'.format(alistamento))
    elif alistamento > 19:
        print('Você passou {} anos do alistamento.'.format(alistamento))
