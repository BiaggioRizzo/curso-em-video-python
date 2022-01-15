#Jogue Par ou Impa com computador, mostre o total de vitórias que ele conseguiu./
#O jogo só será interrompido quando o Jogador perder

from random import randint

vitoria = 0
while True:
    jogador = int (input('Digite um número: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ''
    while tipo not in "PpIi":
        tipo = str(input("Escolha se é Par ou Impa: ")).strip()[0]

    if tipo == 'P':
        if total % 2 == 0:
            vitoria +=1
            print("Você ganhou!")
        else:
            break
    elif tipo == 'I':
        if total % 2 == 1:
            vitoria +=1
            print("Você ganhou!")
        else:
            break