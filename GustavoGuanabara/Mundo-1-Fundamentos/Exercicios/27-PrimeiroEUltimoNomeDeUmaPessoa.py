# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente.

# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

from gettext import find


nome = str(input('Nome: ')).split()

pNome = nome[0]
uNome = nome[-1]
print('''
Primeiro nome: {}
Ultimo nome: {}
'''.format(pNome,uNome))