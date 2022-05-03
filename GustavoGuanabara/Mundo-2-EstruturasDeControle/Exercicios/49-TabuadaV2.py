# Refaça o DESAFIO 009, mostrando a tabuada 
# de um número que o usuário escolher, só que 
# agora utilizando um laço for.

entrada = int(input('Esolha um número para ver a tabuada: '))
n = 0
for i in range(10):
    n += 1
    tabuada = entrada * n
    print('Tabuada de {} x {} = {}'.format(entrada, n, tabuada))