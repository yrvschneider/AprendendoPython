# Crie um programa que leia duas notas de um aluno e calcule
#  sua média, mostrando uma mensagem no final, de acordo com 
# a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))

media = (n1 + n2)/2

if media < 5:
    print('REPROVADO! Sua Media foi de {}'.format(media))
elif media > 5 and media < 7:
    print('RECUPERAÇÃO! Sua Media foi de {}'.format(media))
else:
    print('APROVADO! Sua Media foi de {}'.format(media))