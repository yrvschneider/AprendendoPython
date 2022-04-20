# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

# Ex: Digite um número: 1834

# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

n = (input('Digite um número entre 0 até 9999: '))
l = len(n)

if(l == 4):
    print('Unidade: {}'.format(n[-1]))
    print('Dezena: {}'.format(n[-2]))
    print('Centena: {}'.format(n[-3]))
    print('Milhar: {}'.format(n[-4]))
elif(l == 3):
    print('Unidade: {}'.format(n[-1]))
    print('Dezena: {}'.format(n[-2]))
    print('Centena: {}'.format(n[-3]))
elif(l == 2):
    print('Unidade: {}'.format(n[-1]))
    print('Dezena: {}'.format(n[-2]))
elif(l == 1):
    print('Unidade: {}'.format(n))
else:
    print('Número não esta conforme dolicitado.')

# Formato que o professor utilizou

# numero = int(input('Informe um número até 9999: '))
# u = numero // 1 % 10
# d = numero // 10 % 10
# c = numero // 100 % 10
# m = numero // 1000 % 10
# print('Analisando o número: {}'.format(numero))
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))