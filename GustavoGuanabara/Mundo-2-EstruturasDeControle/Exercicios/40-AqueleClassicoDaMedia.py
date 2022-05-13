# Crie um programa que leia duas notas de um aluno e calcule
#  sua média, mostrando uma mensagem no final, de acordo com 
# a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1+n2)/2

if media < 5:
    print('''
    Nota 1: {}
    Nota 2: {}
    Media: {}
    Você foi REPROVADO!
    '''.format(n1,n2,media))
elif media <= 6.9:
    print('''
    Nota 1: {}
    Nota 2: {}
    Media: {}
    Você esta de RECUPERAÇÃO!
    '''.format(n1,n2,media))
elif media >= 7:
    print('''
    Nota 1: {}
    Nota 2: {}
    Media: {}
    Você foi APROVADO!
    '''.format(n1,n2,media))