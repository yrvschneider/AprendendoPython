# Crie um programa que mostre na tela 
# todos os números pares que estão no 
# intervalo entre 1 e 50.

n1 = int(input('Inicia em: '))
n2 = int(input('Termina em: '))

for i in range(n1, n2+1):
    if i % 2 == 0:
        print(i, end=' ')