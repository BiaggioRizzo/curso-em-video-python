'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios
Guarde esses resultados em um dicionário. No final coloque o dicionário em ordem
Sabendo que o vencedor tirou o maior número no dado
'''
from random import randint
from time import sleep
from operator import itemgetter

dicionario = {
    'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6)}

for keys ,valor in dicionario.items():
   print(f'{keys} tirou o número {valor} no dado.')
   sleep(1)
#sorted ele ordena em outro dicionário
#função itemgetter ele seleciona a posição do dicionário que será ordenado 
ranking = list()
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print('-=' * 10)
print(f'{"RANKING":^20}')
print('-=' * 10)
for index, valor in enumerate(ranking):
    print(f'{index+1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)

'''
Não funciona, pois não consegui fazer uma interação e adicionar novos valores
for jogador in range(1,5):
    numeroSorteado = randint(1,6)
    print(f'Jogador Nº {jogador} tirou o número: {numeroSorteado}')
    dicionario['Jogador'] = jogador
    dicionario['resultado'] = numeroSorteado
    sleep(1)
'''