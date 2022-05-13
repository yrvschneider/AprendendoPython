# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todos as letras maisculas.
# O nome com todas letras minusculas.
# Quantas letras ao todo (sem considerar os espaços).
# Quantas letras tem o primeiro nome.


nome = str(input('Digite seu nome: '))

print('''
Letras Minusculas: {}
Letras Maiusculas: {}
Total de letras: {}
Quantas letras tem o primeiro nome: {}
'''.format(nome.lower(),nome.upper(),len(''.join(nome.split())),len(nome.split(' '))))