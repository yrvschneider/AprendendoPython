# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.


dis = float(input('Qual será a distancia da viagem? '))

if(dis <= 200):
    print('Valor da pasagem é: R${:.2f}'.format(dis * 0.50))
else:
    print('Valor da passagem é: R${:.2f}'.format(dis * 0.45))