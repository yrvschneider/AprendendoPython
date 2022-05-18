# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maiorPeso = 0
menorPeso = 100000000000

for i in range(1,6):
    peso = float(input('Qual peso? '))

    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso
print('''
    Mior peso {:.3f}kl
    Menor peso {:.3f}kl
'''.format(maiorPeso,menorPeso))