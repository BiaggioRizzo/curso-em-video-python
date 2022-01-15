#faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteio() e somaPar(). A primeira função vai sortear 5 número e vai coloca-los
#dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for sorteio in range(6):
        sorteio = randint(1,20)
        lista.append(sorteio)
        print(f'{sorteio}',end=' ',flush=True)
        sleep(0.3)
    #somaPar(lista) caso deseja chamar a função somaPar
    print()

def somaPar(lista):
    resultado = 0
    for valor in lista:
        if valor % 2 == 0:
            resultado += valor
    print(f'Soma dos valores pares da lista {lista}, foi no total de {resultado}')


numeros = []

sorteia(numeros)
somaPar(numeros)