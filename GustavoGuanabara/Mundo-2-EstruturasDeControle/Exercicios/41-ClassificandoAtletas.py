# A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre 
# sua categoria, de acordo com a idade.

# Até 9 anos: MIRIM
# Até 14 ano: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date, datetime
ano = int(input('Ano de Nascimento: '))

idade = date.today().year - ano

if idade < 7:
    print('Atleta menor que 7 anos, não pode participar.')
elif idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 20:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')
