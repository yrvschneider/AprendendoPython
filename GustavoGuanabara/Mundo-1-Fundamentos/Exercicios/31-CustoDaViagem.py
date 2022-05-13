# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.

distancia = 201

if distancia <= 200:
    soma = 0.50 * distancia
    print('''
    Sua passagem ira custar R${}.
    Você ira viajar {}km'''.format(soma,distancia))
else:
    soma = 0.45 * distancia
    print('''
    Sua viagem ira custar R${}.
    Você ira viajar {}km
    '''.format(soma,distancia))