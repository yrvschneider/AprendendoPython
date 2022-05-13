# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Number: '))

tabu = 0
print('''

_____Tabuada_____

''')
for i in range(1,11):
    tabu = n * i
    print('{} * {} = {}'.format(n,i,tabu))