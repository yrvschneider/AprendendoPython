# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(1250.00)

if(salario > 1250.00):
    print('Seu salario terá 10% de aumento saidno de {:.2f} para R${:.2f}, tendo R${:.2f} de aumento.'.format(salario,salario+(salario*(10/100)),salario*(10/100)))
elif(salario <= 1250.00):
    print('Seu salario terá 15% de aumento saidno de {:.2f} para R${:.2f}, tendo R${:.2f} de aumento.'.format(salario,salario+(salario*(15/100)),salario*(15/100)))