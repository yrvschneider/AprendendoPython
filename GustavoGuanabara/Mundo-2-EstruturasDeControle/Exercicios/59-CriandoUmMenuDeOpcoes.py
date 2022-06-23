# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do Programa

# Seu programa deverá realizar a opereção solicitada em cada caso.

n1 = 0
n2 = 0
opcoes = 0
while opcoes != 5:
    n1 = int(input('1º Valor: '))
    n2 = int(input('2º Valor: '))
    opcoes = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior valor
    [4] Novos Valores
    [5] Sair
    '''))
    
    if opcoes == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif opcoes == 2:
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    elif opcoes == 3:
        if n1 > n2:
            print('{} <> {} = {} é o maior'.format(n1,n2,n1))
        elif n1 < n2:
            print('{} <> {} = {} é o maior!'.format(n1,n2,n2))
        elif n1 == n2:
            print('{} e {} são valores iguais.'.format(n1,n2))
    elif opcoes == 4:
        continue
print('FIM')