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

print('Digite uma Frase para ver se ela é um Palíndromo.')
frase = str(input('Digite: ').upper().replace(' ', ''))
pali = frase[::-1]

if pali == frase:
    print('É um Palíndromo!')
    print(pali)
else:
    print('Não é um Palíndromo!')
    print(pali)