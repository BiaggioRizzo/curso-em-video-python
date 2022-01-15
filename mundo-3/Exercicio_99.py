# Faça um programa que tenha uma função chamada maior() que recebe vários
# números inteiros. Verifique qual é o maior número deles;
from time import sleep

def maiorLista(lista):
    tamanho = len(lista)
    print(f'{lista} foram informados {tamanho} valores ao todo.', end=' ')
    maiorValor = 0
    for valor in lista:
        if valor > maiorValor:
            maiorValor = valor
    print(f'Maior valor informado foi {maiorValor}')


def maior(* tuplas):
    tamanho = len(tuplas)
    print(f'{tuplas} foram informados {tamanho} valores ao todo.', end=' ')
    maiorValorTupla = 0
    for valor in range(len(tuplas)):
        if maiorValorTupla < tuplas[valor]:
            maiorValorTupla = tuplas[valor]
    print(f'Maior valor informado foi {maiorValorTupla}')


def respostaProfessor (* num):
    count = maior = 0
    print('\n Analisamos os valores passados...')
    for valor in num:
        print(f'{valor}', end='', flush=True)
        sleep(0.3)
        if count == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += 1
    print(f'Foram informados {count} valores ao todo.')
    print(f'Maior valor informado foi {maior}.')


# Lista
valores = [2,6,4,8,16]
maiorLista(valores)
valores = [28,46,466,84,16]
maiorLista(valores)
print()

#Tuplas
maior(9,8,33,4,10,15)
maior(92,89,32,82,10,34)


