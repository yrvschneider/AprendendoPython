# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km/h acima do limite.


velo = float(input('Digite a velocidade que o carro passou: '))

if(velo > 80):
    multa = float((velo - 80) * 7)
    print('Você tomou uma multa de R${:.2f}'.format(multa))
else:
    print('Passou dentro da velocidade permitida')

# Formula do Professor.

# velocidade = float(input('Qual é a velocidade do carro? '))

# if velocidade > 80:
#     print('Multado! Você excedeu o limite de 80km/h')
#     multa = (velocidade - 80) * 7
#     print('Valor da multa R${:.2f}'.format(multa))
# print('Tenha um bom dia! Dirija com seguraça!')