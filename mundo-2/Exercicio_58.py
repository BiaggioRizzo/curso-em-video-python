#Refazer o execicio 28 e acerta qual número que o computador escolher de 0 a 10

from random import randint

sorteio = randint(0,10)
tentativas = 0
palpite = ''
while sorteio != palpite:
    palpite = int(input('Digite o seu palpite: '))
    if palpite > sorteio:
        print('Menos')
    else:
        print('Mais')
    tentativas += 1

print('Acertou com {} tentativas'.format(tentativas))

'''  Ou
from random import randint

sorteio = randint(0,10)
tentativas = 0
acertou = False
while not acertou:
    palpite = int(input('Digite o seu palpite: '))
    if palpite == sorteio:
        acertou = True
        
    else:
        if palpite < sorteio:
            print('Mais...Tente novamente')
        else:
            print('Menos...Tente novamente')
    tentativas += 1

print('Acertou com {} tentativas'.format(tentativas))
'''