# Faça um programa que mostre na tela uma contagem regressiva 
# para o estouro de fogos de artificio, indo de 10 até 0, 
# com uma pausa de 1 segundo entre eles.

import time
print('Contagem regressiva para os Fogos.')
tempo = 10

for i in range(0, 11):
    print(tempo)
    time.sleep(1)
    tempo -= 1
print('Inicia os Fogos!')

# for i in range(10, -1, -1):
#     time.sleep(1)
#     print(i)
# print('BUM! BUM! BUM!')