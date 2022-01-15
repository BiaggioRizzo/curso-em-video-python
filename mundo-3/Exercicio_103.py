#Crie uma função chamada ficha() com dois parâmetros opcionais. o nome de um jogador e quantos gols ele marcou.
#Deve mostrar a ficha do jogador mesmo se algum dado não tenha sido informado corretamente.

def ficha(nomeJogador='<desconhecido>', gols=0):
    print(f'O jogador {nomeJogador} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: '))
golsMarcado = int(input('Número de gols: '))
print('Preenchendo todos os parâmetros:')
ficha(jogador,golsMarcado)
print('Preenchendo o parâmetro jogador:')
ficha(jogador)
print('Preenchendo o parâmentro gols.')
ficha(gols=golsMarcado)
print('Preenchendo nenhum parâmetro.')
ficha()
