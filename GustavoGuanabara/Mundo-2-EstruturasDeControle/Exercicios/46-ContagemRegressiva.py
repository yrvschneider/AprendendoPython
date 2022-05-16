# Faça um programa que mostre na tela uma contagem regressiva 
# para o estouro de fogos de artificio, indo de 10 até 0, 
# com uma pausa de 1 segundo entre eles.

import time

for i in range(10, 0, -1):
    time.sleep(1)
    print(i)
for e in range(0,10):
    time.sleep(0.1)
    print('BOOM BOOM BOOM CABOOM')