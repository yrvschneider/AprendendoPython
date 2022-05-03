# Crie um programa que mostre na tela 
# todos os números pares que estão no 
# intervalo entre 1 e 50.

n = 0

for i in range(0, 50):
    n += 1
    par = n % 2
    if par == 0:
        print(n)
