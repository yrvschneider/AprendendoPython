# Escreva um programa que pergunte a quantidade de km
#  percorridos por um carro alugado e a quantidade de
#  dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

km = int(input('Km percorridos: '))
dias = int(input('Dias: '))

valorDia = 60
valorKm = 0.15

print('''
Ficou com o carro por {} dias e rodou {}km.
O carro custa R${:.2f} por dia e R${:.2f} por km rodado.
O valor a ser pago é R${:.2f}.
'''.format(dias,km,valorDia,valorKm,(valorDia*dias)+(valorKm*km)))