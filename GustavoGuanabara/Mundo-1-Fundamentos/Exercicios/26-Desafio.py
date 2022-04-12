# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

frase = input('Digite uma frase: ')
f = frase.lower()

print('Quantas vezes aparece a letra `A`? {} vezes'.format(f.count('a')))
print('Em que posição ela aparece a primeira vez? Posição {}'.format(f.index('a')))
print('Em que posição ela aparece a ultima vez? Posição {}'.format(f.rfind('a')))