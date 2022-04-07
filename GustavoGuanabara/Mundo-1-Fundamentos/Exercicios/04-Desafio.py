# Faça uma programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

entrada = input('Digite algo: ')

print('Tipo primitivo: ', type(entrada))
print('Só tem espaços? ', entrada.isspace())
print('É um número? ', entrada.isnumeric())
print('É alfabetico? ', entrada.isalpha())
print('É alfanumerico? ', entrada.isalnum())
print('Está em maisculas? ', entrada.isupper())
print('Está em minusculas? ', entrada.islower())
print('Está capitalizada? ', entrada.istitle())