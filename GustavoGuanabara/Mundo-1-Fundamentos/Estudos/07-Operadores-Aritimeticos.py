print('Operadores Aritméticos')
print(5 + 2, ' - Adição')
print(5 - 2, ' - Subtração')
print(5 * 2, ' - Multiplicação')
print(5 / 2, ' - Divisão')
print(5 ** 2, ' - Potencia')
print(5 // 2, ' - Divisão Inteira')
print(5 % 2, ' - Resto da Divisão')

print()

print('Ordem de Precedência')
print('Quando tiver estas precedencias dos operadores, tem que sempre ler em primeiro, nesta ordem. Forma da leitura é da direita para a esquerda')
print('1º ()')
print('2º **')
print('3º *, /, //, %')
print('4º +, -')

n1 = int(input('Um valor: '))
n2 = int(input('Segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a multiplicação é {} e a divisão é {:.2f}'.format(s,m,d)) # utilizando end='' ele ira juntar o print de baixa com este print, sem quebrar a linha.
print('Divisão Inteira {} e Potencia {}'.format(di,e))


# # Extra
# nome = 'Yuri'
# print('Prazer em conhecer você {:20}!'.format(nome))
# print('Prazer em conhecer você {:>20}!'.format(nome))
# print('Prazer em conhecer você {:<20}!'.format(nome))
# print('Prazer em conhecer você {:^20}!'.format(nome))
# print('Prazer em conhecer você {:=^20}!'.format(nome))