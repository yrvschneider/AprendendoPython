# Faça um programa que calcule a soma entre 
# todos os números impares que são múltiplos 
# de três e que se encontram no intervalo 
# de 1 até 500.

for i in range(1, 501):
    print(end='.')
    if i%3 == 0:
        soma = i + i
        print(i, end=' ')
print('''
Soma de todos os números impares multiplos por tres: {}
'''.format(soma))