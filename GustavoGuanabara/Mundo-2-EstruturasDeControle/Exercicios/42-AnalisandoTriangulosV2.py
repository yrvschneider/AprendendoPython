# Refaça o DESAFIO 35 dos triângulos, acrecentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

reta1 = float(input('Primeira Reta: '))
reta2 = float(input('Segunda Reta: '))
reta3 = float(input('Terceira Reta: '))

if reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta1+reta2:
    print('Forma um Triangulo')
    if reta1 == reta2 and reta2 == reta3:
        print('Equilátero: Quando todos os lados do triangulo são iguais.')
    elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print('Escaleno: Quando todos os lados do tringulo é diferentes.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Isóceles: Quando tem dois lados iguais no triangulo.')
else:
    print('Não forma um triangulo.')