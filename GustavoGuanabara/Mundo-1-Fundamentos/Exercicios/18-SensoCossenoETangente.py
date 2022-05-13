# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math

n = float(input('Digite o Angulo: '))

seno = math.sin(math.radians(n))
cosseno = math.cos(math.radians(n))
tangente = math.atan(math.radians(n))

print('''
Seno: {:.2f}
Cosseno: {:.2f}
Tangente: {:.2f}
'''.format(seno, cosseno, tangente))