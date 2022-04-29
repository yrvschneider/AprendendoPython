# Um professor quer sortear um dos seus quatro alunos para apagar oquadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

# alunos = ['Bruno', 'Aline', 'Mateus', 'Ricardo']
n1 = str(input('Prumeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
alunos = [n1, n2, n3, n4]
escolhido = random.choice(alunos)
print('O aluno escolhi foi: {}'.format(escolhido))
