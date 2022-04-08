# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

# alunos = ['Bruno', 'Aline', 'Mateus', 'Ricardo']
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
alunos = [n1, n2 ,n3, n4]

random.shuffle(alunos)

print('Segue a lista da ordem da apresentação do trabalho')
print(alunos)