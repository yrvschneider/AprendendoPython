# Escreva um programa que pergunte a quantidade de km
#  percorridos por um carro alugado e a quantidade de
#  dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

KMpercorrido = int(input('Quantos KM percorrido? '))
DiasComCarro = int(input('Quantos dias ficou com o carro? '))

Carro = 60
km = 0.15

print('''
Ficou com o Carro por {} dias.
Percorreu {} km.
Valor a pagar pelo aluguel R${:.2f}
'''.format(KMpercorrido, DiasComCarro, (Carro*DiasComCarro)+(km*KMpercorrido)))