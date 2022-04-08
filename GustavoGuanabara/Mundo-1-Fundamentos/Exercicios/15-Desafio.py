# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.


km = float(input('Quantos km o carro percorreu? '))
dias = int(input('Quantos dias ficou com o carro? '))

valor = (dias * 60) + (0.15 * km)

print('O Sr. ficou com o carro por {} dias e rodou {} km. O valor a ser pago é R${:.2f}'.format(dias,km,valor))