# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = int(input('Temperatura: '))

print('''
Temperatura em Grau Celsius: {} ºC
Temperatura em Fahrenheit: {:.0f} ºF
'''.format(c, (c * 9/5) + 32))