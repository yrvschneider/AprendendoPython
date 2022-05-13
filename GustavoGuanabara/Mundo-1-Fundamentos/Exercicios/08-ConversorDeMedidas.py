# Escreva um programa que leia um valor em
#  metros e o exiba convertido em centimetros e milimetros.

metros = int(input('Quantos Metros: '))



print('''
    Metro: {}m
    Centimetros: {}cm
    Milimetros: {}mm
'''.format(metros, metros*100,metros*1000))
