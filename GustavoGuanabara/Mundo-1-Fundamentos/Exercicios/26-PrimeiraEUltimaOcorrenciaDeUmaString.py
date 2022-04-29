# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

frase = input('Digite uma frase: ').lower().strip()

print('Quantas vezes aparece a letra `A`? {} vezes'.format(frase.count('a')))
print('Em que posição ela aparece a primeira vez? Posição {}'.format(frase.find('a')+1))
print('Em que posição ela aparece a ultima vez? Posição {}'.format(frase.rfind('a')+1))