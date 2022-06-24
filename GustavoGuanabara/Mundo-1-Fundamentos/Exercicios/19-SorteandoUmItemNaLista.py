# Um professor quer sortear um dos seus quatro alunos para apagar oquadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

alunos = ['Joãozinho', 'Carla', 'Pedro', 'Kelly']

print('''
Aluno sorteado para apagar o quadro "{}"
'''.format(random.choice(alunos)))