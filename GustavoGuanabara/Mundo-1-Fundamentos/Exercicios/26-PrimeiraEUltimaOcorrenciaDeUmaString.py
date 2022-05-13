# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

frase = 'Interagir com clientes irritados pode ser um grande desafio. Manter uma atitude positiva é fundamental, a fim de estimular o bom humor do cliente. A todo o momento a linguagem usada ao interagir com o cliente é muito importante, sobretudo quando estão irritados. As frases a seguir demonstram como lidar melhor com essas situações:'.lower()

letra = frase.count('a')
aP = frase.find('a')
aU = frase.rfind('a')

print('''
Letra 'a' aparece {}x
Posição {} da primeira letra 'a' 
Ultima posição {} da letra 'a' 
'''.format(letra,aP,aU))