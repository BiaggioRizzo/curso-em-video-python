#Gere 5 números aleatórios e coloque dentro de uma tupla, depois liste os números e indique qual foi o maior e menor.

from random import randint
sorteio =((randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),
(randint(1,10)))
#print(f'Os números sorteados foram: {sorteio}')
print('Os números sorteados foram:', end='')
for i in sorteio:
    print(f' {i} ', end='')

print(f'\nMaior valor sorteado foi {max(sorteio)}')
print(f'Menor valor sorteado foi {min(sorteio)}')