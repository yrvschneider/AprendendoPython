# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todos as letras maisculas.
# O nome com todas letras minusculas.
# Quantas letras ao todo (sem consiferar os espaços).
# Quantas letras tem o primeiro nome.


from posixpath import split

nome = str(input('Digite seu nome completo: '))
# nome = 'Yuri Ricardo Verardo Schneider'

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
primeiroName = nome.split()
print(len(primeiroName[0]))