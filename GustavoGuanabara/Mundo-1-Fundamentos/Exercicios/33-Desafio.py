# Faça um programa que leia tres números e mostre qual é o ''maior'' e qual é o ''menor''

n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
n3 = int(input('Digite o Terceiro Número: '))

if(n1 > n2 and n1 > n3):
    print('Número {} é maior número'.format(n1))
elif(n2 > n1 and n2 > n3):
    print('Número {} é maior número'.format(n2))
elif(n3 > n1 and n3 > n2):
    print('Número {} é o maior número'.format(n3))