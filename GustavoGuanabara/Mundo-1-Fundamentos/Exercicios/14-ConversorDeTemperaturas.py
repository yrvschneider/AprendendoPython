# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input('temperatura em Grau Celsius: '))

f = (c * 9/5)+32

print('Graus Celsius {:.1f}°C para Fahrenheit é {:.1f}°F'.format(c,f))