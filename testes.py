# nome = input('Digite seu nome: ')
# print('Olá, {}!'.format(nome))

# n1 = int(input('Digite o primeiro numero: '))
# n2 = int(input('Digite o segundo numero: '))
# soma = n1 + n2
# print('A soma entre os numeros {} e {}, é {}'.format(n1,n2,soma))

entrada = input('Digite qualquer palavra: ')

print('Tipo primitivo desse valor é: ', type(entrada))
print('Só tem espaços? ', entrada.isspace())
print('É um número? ', entrada.isnumeric())
print('É alfabetico? ', entrada.isalpha())
print('É alfanumerico? ', entrada.isalnum())
print('Está em maisculas? ', entrada.isupper())
print('Esta em minusculas? ', entrada.islower())
print('Esta capitalizada? ', entrada.istitle())
