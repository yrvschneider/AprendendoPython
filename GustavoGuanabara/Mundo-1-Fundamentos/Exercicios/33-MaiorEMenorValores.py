# Faça um programa que leia tres números e mostre qual é o ''maior'' e qual é o ''menor''

# n1 = int(input('Digite o Primeiro Número: '))
# n2 = int(input('Digite o Segundo Número: '))
# n3 = int(input('Digite o Terceiro Número: '))

# if(n1 > n2 and n1 > n3):
#     print('Número {} é o MAIOR número'.format(n1))
# elif(n2 > n1 and n2 > n3):
#     print('Número {} é o MAIOR número'.format(n2))
# elif(n3 > n1 and n3 > n2):
#     print('Número {} é o MAIOR número'.format(n3))

# if n1 < n2 and n1 < n3:
#     print('Número {} é o MENOR número'.format(n1))
# elif n2 < n1 and n2 < n3:
#     print('Número {} é o MENOR número'.format(n2))
# elif n3 < n1 and n3 < n2:
#     print('Número {} é o MENOR número'.format(n3))

# Formula do Professor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificar quem é o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificar quem é o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O MENOR valor {}'.format(menor))
print('O MAIOR valor {}'.format(maior))