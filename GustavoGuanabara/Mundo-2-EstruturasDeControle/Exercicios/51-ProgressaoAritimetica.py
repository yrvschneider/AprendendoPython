# Desenvolva um programa que leia o primeiro 
# termo e a razão de uma PA. No final, mostre 
# os 10 primeiros termos dessa progressão.
# Progressão Aritimetica.

t = int(input('Digite o Termo: '))
r = int(input('Digite a Razão: '))

for i in range(0, 10):
    t += r
    print('PA: {}'.format(t))

# primeiro = int(input('Primeiro Termos: '))
# razao = int(input('Razão: '))
# decimo = primeiro + (10 - 1) * razao

# for i in range(primeiro, decimo + razao, razao):
#     print('{}'.format(i), end=' > ')
# print('FIM!')