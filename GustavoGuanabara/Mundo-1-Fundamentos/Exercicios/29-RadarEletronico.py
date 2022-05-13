# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km/h acima do limite.

velocidade = int(input('km/h: '))

maxima = 80
multa = 7

if velocidade > 80:
    multa = (velocidade-maxima)*multa
    print('''
    Recebeu multa por ultrapassar {}km/h.
    Sua velocidade {}km/h
    Multa R${:.2f}
    '''.format(maxima,velocidade,multa))
else:
    print('Tenha uma Boa Viagem!')