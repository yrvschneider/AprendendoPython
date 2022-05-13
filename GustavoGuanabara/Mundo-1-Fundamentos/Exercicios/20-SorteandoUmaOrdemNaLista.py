# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = ['Yuri', 'Sara', 'Lucas', 'Schneider']

random.shuffle(alunos)

for aluno in alunos:
    print(aluno)