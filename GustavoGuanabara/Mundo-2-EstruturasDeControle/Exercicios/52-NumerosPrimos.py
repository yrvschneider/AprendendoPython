# Faça um programa que leia um número inteiro 
# e diga se ele é ou não um número primo.

n = int(input('Número: '))
total = 0
if n > 1:
    for i in range(1, n + 1):
         if n % i == 0:
            total += 1
if total == 1 or total == 2:
    print('Primo')
else:
    print('Não')