# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('Vamos converter Decimal para Binário, Octal ou Hexadecimal!')
print()
n = int(input('Digite um número inteiro: '))
c = int(input('Digite 1 para Binário, 2 para Octal e 3 para Hexadecimal. '))

if c == 1:
    binario = bin(n)
    print('Binário: {}'.format(binario[2::]))
elif c == 2:
    octal = oct(n)
    print('Octal: {}'.format(octal[2::]))
else:
    hexadecimal = hex(n)
    print('Hexadecimal: {}'.format(hexadecimal[2::]))