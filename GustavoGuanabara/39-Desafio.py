# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade.

# Se ele ainda vai se alsitar ao serviço militar.
# Se é a hora de se alsitar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Informe ano de nascimento: '))

alistamento = date.today().year - ano

if alistamento < 18:
    print('Ainda falta {} anos para se Alistar no Serviço Militar.'.format(18 - alistamento))
elif alistamento == 18:
    print('Já é hora de se Alistar no Serviço Militar. Você já tem {} anos'.format(alistamento))
else:
    print('Você já passou do tempo de se Alistar no Serviço Militar.')