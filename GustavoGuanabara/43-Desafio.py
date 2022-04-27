# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

print('Exemplo: Altura 1.72 - Peso 76.90')
altura = float(input('Digite sua altura em Altura: '))
kg = float(input('Digite seu peso: '))

imc = kg / (altura * altura)

if imc < 18.5:
    print('IMC {:.1f} Abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC {:.1f} Peso Ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC {:.1f} Sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC {:.1f} Obesidade!')
else:
    print('IMC {:.1f} Obesidade Mórbida!'.format(imc))