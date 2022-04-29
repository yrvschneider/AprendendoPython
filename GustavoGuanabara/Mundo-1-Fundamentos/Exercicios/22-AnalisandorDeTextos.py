# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todos as letras maisculas.
# O nome com todas letras minusculas.
# Quantas letras ao todo (sem consiferar os espaços).
# Quantas letras tem o primeiro nome.


from posixpath import split

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
# print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # Formato que o professor utilizou
# print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # Formato que o professor utilizou
primeiroName = nome.split()
print('Seu primeiro nome é {}'.format(len(primeiroName[0])))