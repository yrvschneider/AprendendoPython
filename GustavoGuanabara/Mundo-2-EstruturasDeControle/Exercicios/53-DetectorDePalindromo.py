# Crie um programa que leia uma frase qualquer
#  e diga se ela é um palíndromo, desconsiderando
#  os espaços.

# Palíndromo é uma frase que pode ler de frente
#  para trás e de trás para frente, dando a mesma
#  coisa na leitura.

# Exemplos
# Apos a Sopa
# A sacada da casa
# O lobo ama o bolo
# Anotaram a data da maratona

entrada = 'Apos a Sopa'

fraseManipulada = entrada.upper().strip().replace(' ', '')
fraseInvertida = fraseManipulada[::-1]

if fraseManipulada == fraseInvertida:
    print('''
    É uma frase Palíndromo!
    Frase digitada: {}
    Frase invertida: {}
    '''.format(entrada, fraseInvertida))
else:
    print('Não é uma frase Palíndromo!')