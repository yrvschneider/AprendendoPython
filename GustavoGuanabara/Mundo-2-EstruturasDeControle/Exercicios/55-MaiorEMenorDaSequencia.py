# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 1000000
for i in range(1,6):
    peso = float(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior, menor))
