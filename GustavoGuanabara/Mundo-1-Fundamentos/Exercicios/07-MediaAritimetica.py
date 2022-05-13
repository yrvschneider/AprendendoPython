# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('1º Nota: '))
n2 = float(input('2º Nota: '))
print('''
    1º Nota {}
    2º Nota {}
    Media {}
'''.format(n1,n2,(n1+n2)/2))