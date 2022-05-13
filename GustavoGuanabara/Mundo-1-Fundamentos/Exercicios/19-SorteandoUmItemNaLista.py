# Um professor quer sortear um dos seus quatro alunos para apagar oquadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

alunos = ['Yuri', 'Sara', 'Lucas', 'Schneider']

sorteio = random.choice(alunos)

print('Aluno sorteado é o(a)',sorteio)