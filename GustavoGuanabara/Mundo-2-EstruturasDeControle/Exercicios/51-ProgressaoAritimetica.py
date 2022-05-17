# Desenvolva um programa que leia o primeiro 
# termo e a razão de uma PA. No final, mostre 
# os 10 primeiros termos dessa progressão.
# Progressão Aritimetica.

termo = int(input('Termo: '))
razao = int(input('Razão: '))

print('1 - {}'.format(termo))
for i in range(2, 11):
    termo += razao
    print('{} - {}'.format(i,termo))