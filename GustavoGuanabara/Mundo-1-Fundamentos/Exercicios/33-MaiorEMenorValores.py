# Faça um programa que leia tres números e mostre qual é o ''maior'' e qual é o ''menor''

n = []

for i in range(0,3):
    n.append(int(input('Número: ')))

print('''
Menor valor: {}
Maior valor: {}
'''.format(min(n),max(n)))