# Refaça o DESAFIO 35 dos triângulos, acrecentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('Comprimento da Primeira Reta: '))
r2 = float(input('Comprimento da Segunda Reta: '))
r3 = float(input('Comprimento da Terceira Reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um Triangulo!')
    if r1 == r2 and r1 == r3:
        print('Equilátero: todos os lados iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles: dois lados iguais')
    else:
        print('Escaleno: todos os lados diferentes')
else:
    print('Não forma um Triangulo!')