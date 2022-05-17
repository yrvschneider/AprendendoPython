# Refaça o DESAFIO 009, mostrando a tabuada 
# de um número que o usuário escolher, só que 
# agora utilizando um laço for.

n = int(input('Número: '))

print('Tabuada')
for i in range(1, 11):
    tabu = n * i
    print('{} * {} = {}'.format(n,i,tabu))