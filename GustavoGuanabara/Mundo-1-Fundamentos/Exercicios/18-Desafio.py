# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math

n = float(input('Digite um número qualquer: '))
seno = math.sin(math.radians(n))
print('O angulo de {} tem o Seno {:.2f}'.format(n,seno))
cosseno = math.cos(math.radians(n))
print('O Angulo de {} tem o Cosseno de {:.2f}'.format(n,cosseno))
tangente = math.tan(math.radians(n))
print('O Angulo de {} tem a Tangnte de {:.2f}'.format(n,tangente))