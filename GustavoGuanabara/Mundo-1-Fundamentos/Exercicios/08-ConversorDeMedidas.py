# Escreva um programa que leia um valor em
#  metros e o exiba convertido em centimetros e milimetros.

n = int(input('Valor: '))

print('''
Metros: {}
Centimetros: {}
Milimetros: {}
'''.format(n, n*100, n*1000))