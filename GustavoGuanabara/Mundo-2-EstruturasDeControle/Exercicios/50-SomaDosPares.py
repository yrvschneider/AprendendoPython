# Desenvolva um programa que leia seis números 
# inteiros e mostre a soma apenas daqueles 
# que forem pares. Se o valor digitado 
# for impar, desconsidere-o.

soma = 0

for i in range(1, 7):
    n = int(input('Número: '))
    if n % 2 == 0:
        soma += n
print('Soma dos números pares digitados: ',soma)