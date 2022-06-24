# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a1 = 'Pedrinho'
a2 = 'Carla'
a3 = 'Joãozinho'
a4 = 'Kelly'

alunos = [a1,a2,a3,a4]
random.shuffle(alunos)

print('''
Ordem dos alunis para apresentação.
{}
'''.format(alunos))