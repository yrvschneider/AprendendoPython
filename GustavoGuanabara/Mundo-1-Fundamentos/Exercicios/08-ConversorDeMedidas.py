# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

valor = float(input('Digite um valor: '))
centi = valor * 100
mili = valor * 1000

print('Convertido para Centimetros: {}cm'.format(centi))
print('Convertido para Milimetros: {}mm'.format(mili))