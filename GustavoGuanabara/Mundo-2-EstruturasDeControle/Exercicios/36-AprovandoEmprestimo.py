# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ele não pode esceder 30% do salário ou então o empréstimo será negado.

ValorCasa = float(input('Valor da casa: R$'))
salario = float(input('Seu salario: R$'))
anosParaPagar = int(input('Quantos anos vai querer pagar? '))

meses = anosParaPagar * 12
trintaporcento = salario*(30/100)
valorMensalCasa = ValorCasa/meses
print('')

if trintaporcento >= valorMensalCasa:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo não aprovado!')

print('''
        Dados informados:
Valor da Casa: R${:.2f}
Salario: R${:.2f}
Quantos anos ira pagar? {} anos
Quantos meses será? {} meses
30% do Salario R${:.2f}
Valor da parcela R${:.2f}
'''.format(ValorCasa, salario, anosParaPagar, meses,trintaporcento,valorMensalCasa))