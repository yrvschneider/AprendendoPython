# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input('Digite a temperatura em °C: '))
f = (c * 9/5) + 32

print('A temperatura em {} °C convertida para {} °F'.format(c,f))