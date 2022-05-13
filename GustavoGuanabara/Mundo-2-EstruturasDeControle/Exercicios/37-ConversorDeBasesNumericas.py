# Escreva um programa que leia um número inteiro qualquer
#  e peça para o usuário escolher qual será a BASE DE CONVERSÃO:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

n = int(input('Digite um número: '))
print('Vamos escolher uma opção para converter o número inteiro para algum da lista abaixo.')
opcao = int(input('[1] = Binário | [2] = Octal | [3] = Hexadecimal | [4] = Mostrar todos '))

bi = '{0:b}'.format(n)
oc = '{0:o}'.format(n)
he = '{0:X}'.format(n)

if opcao == 1:
    print('Número {} para Binário {}'.format(n, bi))
elif opcao == 2:
    print('Número {} para Octal {}'.format(n, oc))
elif opcao == 3:
    print('Número {} para Hexadecimal {}'.format(n,he))
elif opcao == 4:
    print('Número {} para Binário {}, Octal {} e Hexadecimal {}'.format(n,bi,oc,he))
else:
    print('Opção errada!')

# =  |	Coloca o sinal na posição mais à esquerda
# b  |	Converte o valor em binário equivalente
# o  |	Converte o valor para o formato octal
# x  |	Converte o valor para o formato Hex
# d  |	Converte o valor dado em decimal
# E  |	Formato científico, com um E em maiúsculas
# X  |	Converte o valor para o formato Hex em maiúsculas