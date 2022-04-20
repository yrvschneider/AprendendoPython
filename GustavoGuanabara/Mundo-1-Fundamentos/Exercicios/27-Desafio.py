# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente.

# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

nome = 'Yuri Ricardo Verardo Schneider'.strip().split()

print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[-1]))