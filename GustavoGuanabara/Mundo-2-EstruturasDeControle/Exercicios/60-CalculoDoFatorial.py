# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5*4*3*2*1 = 120

from audioop import mul


n = int(input('valor: '))
c = 0
mult = n

while c != n-1:
    c += 1
    print('{}'.format(mult), end=' * ')
    mult *= c
    print('{} = {}'.format(c,mult))
print('FIM')