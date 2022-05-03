# Faça um programa que calcule a soma entre 
# todos os números impares que são múltiplos 
# de três e que se encontram no intervalo 
# de 1 até 500.
quantidade = 0
soma = 0
for i in range(0, 501):
    if i % 3 == 0:
        print(i, end=' ')
        soma = soma + i

print('''
    
    Quantos números são IMPAR: {}
    Soma de todos os números IMPAR: {}
    '''
    .format(quantidade, soma))