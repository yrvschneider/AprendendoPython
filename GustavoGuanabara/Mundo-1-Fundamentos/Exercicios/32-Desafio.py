# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano para ver se ele é Bissexto: '))

if(0 == ano%4 and 0 == ano%100 and 0 == ano%400):
    print('Ano Bissexto')
else:
    print('Não é ano Bissexto')