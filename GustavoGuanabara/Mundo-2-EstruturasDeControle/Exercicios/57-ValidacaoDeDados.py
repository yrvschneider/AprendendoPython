# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
# Caso esteja errado, peça para digitar novamente até ter um valor valido.

sexo = ''

while sexo != 'F' or 'M':
    sexo = str(input('Escolha um sexo M/F: ')).upper()

    if sexo == 'F':
        print('Escolheu Feminino!')
        break
    elif sexo == 'M':
        print('Escolheu Masculino!')
        break
    elif sexo != 'F' or 'M':
        print('Escolha a opção correta!')