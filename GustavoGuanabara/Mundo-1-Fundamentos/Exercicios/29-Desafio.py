# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km/h acima do limite.


velo = int(input('Digite a velocidade que o carro passou: '))

if(velo > 80):
    multa = float((velo - 80) * 7)
    print('Você tomou uma multa de R${:.2f}'.format(multa))
else:
    print('Passou dentro da velocidade permitida')