#Faça um programa que ajude o jogador na mega sena a criar palpites.
# o programa vai perguntar quantos jogo irão ser feitos e vai sortear 6 numero
# entre 1 a 60 para cada jogo. No final cadastre tudo em uma lista composta
from random import randint
from time import sleep
jogo = []
quantidadeJogos = int(input('Quanto jogos você deseja criar? '))

for quantidade in range(1,quantidadeJogos + 1):
    for qtd in range(6):
        numeroSorteado = randint(1,60)
        if numeroSorteado not in jogo:
            jogo.append(numeroSorteado)
    jogo.sort()
    print(f'Jogo número {quantidade}: {jogo}') 
    jogo.clear()

### Resposta do professor #
lista = list()
jogos = list()
total = 1

while total <= quantidadeJogos:
    count = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for index , linhaJogo in enumerate(jogos):
    print(f'Jogo {index+1}: {linhaJogo}')
    sleep(2)