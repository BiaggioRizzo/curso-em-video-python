#Melhore o exercicio 93 para ele ler vários jogadores, incluindo em um sistema 
#de visualização de detalhes do aproveitamento de cada jogador.
fichaJogador = {}
listaGol = []
time = list()

while True:
    fichaJogador.clear()
    listaGol.clear()
    fichaJogador['nome'] = str(input('Digite o nome do jogador: '))
    partidasJogadas = int(input(f'Quantas partidas {fichaJogador["nome"]} jogou? '))
    
    for partidas in range(1, partidasJogadas + 1):
        listaGol.append(int(input(f'Quantos gols feitos na partida {partidas}: ')))

    fichaJogador['gols'] = listaGol[:]
    fichaJogador['total'] = sum(listaGol)
    time.append(fichaJogador.copy())
    
    while True:
        reposta = str(input("Desja continuar? [S/N] ")).upper()
        if reposta in 'SN':
            break
        print("Digite apenas o valor 'S' ou 'N' ")
    if reposta == 'N':
        break

print('-='*25)
print('cod ',end='')
for index in fichaJogador.keys():
    print(f'{index:<15}', end='')
print()
for numero , valor in enumerate(time):
    print(f'{numero:<4}', end='')
    for dados in valor.values():
        print(f'{str(dados):<15}', end='')
    print()
print('-='*25)

while True:
    busca = int(input("Qual jogador você deseja saber mais informações? {Número 999 sai do programa.} "))
    if busca == 999:
        break
    if busca > len(time):
        print(f'Erro! Não existe jogador com código {busca}.')
    else:
        print(f'O jogador {time[busca]["nome"]} jogou {len(time[busca]["gols"])} partidas.')
        for partida in range(len(time[busca]['gols'])):
            print(f'\tNa partida {partida+1}, fez {time[busca]["gols"][partida]} gols.')
        print(f'O jogador {time[busca]["nome"]} fez um total de {time[busca]["total"]} de gols.')