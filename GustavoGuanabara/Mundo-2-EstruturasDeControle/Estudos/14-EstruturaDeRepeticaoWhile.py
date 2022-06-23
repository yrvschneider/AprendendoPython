# c = 1
# while c < 10:
#     print(c, end=' ')
#     c += 1
# print('FIM!')

# c = 1
# while c != 0:
#     c = int(input('Número: '))
# print('FIM')

# r = 'S'
# while r == 'S':
#     n = int(input('Número: '))
#     r = str(input('QUer continuar? S/N' )).upper()
# print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Valor: '))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar +=1
print('FIM - {} PAR e {} IMPARES'.format(par,impar))