# Refaça o DESAFIO 51, lendo o promeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Termo: '))
razao = int(input('Razão: '))

c = 0

while c != 10:
    c += 1
    print('{} - {} + {}'.format(c,razao,termo), end=' = ')
    termo += razao
    print('{}'.format(termo))