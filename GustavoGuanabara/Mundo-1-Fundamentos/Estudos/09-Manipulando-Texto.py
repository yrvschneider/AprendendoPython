# Se escrevemos fras = 'Curso em video Python', ele ira salvar na memoria do computador para mostrar na tela. Mas quando ele salva na memoria, ele ira salvar letra por letra e dar indices a eles. Os espços tambem ira mocupar espaço na memoria, então eles ira mter um indice tambem.
# Exp:      [C],[u],[r],[s],[o],[ ],[e],[m],[ ],[V],[i],[d],[e],[o],[ ],[P],[y],[t],[h],[o],[n]
# Indices    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20

frase = 'Curso em Video Python'
frase1 = '   Aprenda Python   '

# Fatiamento

print(frase[9])
print(frase[9:13]) # Ele ira pegar do 9 até o 12, o 13 ele não ira trazer, para ele trazer o 13, tem que colocar até o indice 14. Ai ira fazer a palavra Video
# Trabalhando com range ele não pega o ultimo valor.
print(frase[9:21]) # Como não existe o 21, ele ira ir até o 20 a onde queremos, sabemos que ele não tras o ultimo indice que mencionamos, por isso colocamos o indice 21. Não é a melhor forma de fazer.
print(frase[9:21:2]) # [9:21:2] o 9 é o indice que ira começar e ira terminar no 21. O que é o 2, ele ira pular dois indices e ira mostrar o proximo indice.
print(frase[:5]) # Ele ira mostrar até o indice 5.
print(frase[15:]) # Ele ira mostrar do 15 até o 20.
print(frase[9::3]) # Aqui ele ira pegar apartir do inicide 9 e ir pulando 3 inidices

# Análise

print(len(frase)) # ira contar quantos indices tem nesta variavel
print(frase.count('o')) # ira contar quantas letras O tem na variavel.
print(frase.count('o', 0, 13)) # aqui ela ira contar quantos O tem até o indice 13. Sabendo que o ultimo valor é ignorado pelo Python.
print(frase.find('deo')) # aqui ele ira mostrar a onde começou esta palavra ou trexo que solicitou.
print(frase.find('Android')) # quando colocar dentro do find uma letra ou palavra que não existe na variavel, ele ira te retornar -1, porque não existe o -1, então esta palavra não existe.
print('Curso' in frase) # Utilizando o in, ele ira te informar se existe a palavra ou letra dentro da varial, te retornando True ou False, lembrando que o Python diferencia de letras maisculas e minusculas.

# Transformação

print(frase.replace('Python', 'Android')) # Utilizando o replace, ele ira alterar a letra ou palavra da variavel. Ele altera, somente neste momento que solicita.
print(frase.upper()) # ira deixar toda a frase em maisculo. 
print(frase.lower()) # ira deixar todas as letras em minusculos.
print(frase.capitalize()) # ele ira jogar todas os caracteres que estão em maisculos para minusculos, deixando somente a primeira letra em maisculo.
print(frase.title()) # Utilizando o title, ele vai deixar palavra por palavra com a inicial maiscula.
print(frase1)
print(frase1.strip()) # Utilizando o strip. ele ira retirar os espaços não utei. deixando somente os espaços entre as palavras.
print(frase1.rstrip()) # Se colocarmos o r (right) no inicio do strip, ele retira os espaços somente pela direito.
print(frase1.lstrip()) # Se colocarmos o l (left) no incio do strip, ele ira retirar os espaços do inicio da frase.

# Divisão

print(frase.split()) # Utilizando o split, ele ira dividir a frase em varios caracteres, a onde estiver espaço ele ira corta e tambem a cada palavra separada, tambem ira iniciar com o indice 0. Exp: como ficaria ['Curso', 'em', 'Video', 'Python']

# Junção

print('-'.join(frase)) # utilizando esta função, ele ira cada palavra com este -.