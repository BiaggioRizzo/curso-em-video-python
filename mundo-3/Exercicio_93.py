'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogodor e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final tudo sera guardado
em um diconário, incluindo o total de gols feitos durante o campeonato.
'''

fichaJogador = {}
listaGol = []
totalRealizado = 0

fichaJogador['nome'] = str(input('Digite o nome do jogador: '))
partidasJogadas = int(input(f'Quantas partidas {fichaJogador["nome"]} jogou? '))
for partidas in range(1, partidasJogadas + 1):
    golRealizado = int(input(f'Quantos gols feitos na partida {partidas}: '))
    listaGol.append(golRealizado)
    totalRealizado += golRealizado

fichaJogador['gols'] = listaGol
fichaJogador['total'] = totalRealizado 
''' Podia realizar a função sum(listaGol) que soma 
todos os valores contidos dentro da lista'''

print('-='*25)
print(fichaJogador)
print('-='*25)

for keys, values in fichaJogador.items():
    print(f'O campo "{keys}" tem o valor {values}.')
print('-='*20, '\n\n')

print(f'O jogador {fichaJogador["nome"]} jogou {len(fichaJogador["gols"])} partidas.')
for partida in range(len(fichaJogador['gols'])):
    print(f'\tNa partida {partida+1}, fez {fichaJogador["gols"][partida]} gols.')
print(f'O jogador {fichaJogador["nome"]} fez um total de {fichaJogador["total"]} de gols.')

''' Outra solução do for para fazer o print da quantidades de partidas mais os gols
O motivo que posso fazer isso é por que a key 'gols' contém uma lista.
for index, values in enumarate(jogador['gols']):
    print(f' Na partida {index}, fez {values} gols.')
'''