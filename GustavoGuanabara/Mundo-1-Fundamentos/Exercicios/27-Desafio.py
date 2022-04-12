# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente.

# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

nome = 'Yuri Ricardo Verardo Schneider'
n = nome.split()


print('Primeiro nome: {}'.format(n[0]))
print('Ultimo nome: {}'.format(n[-1]))