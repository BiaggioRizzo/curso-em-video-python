''' Criar um programa que leia vários números e armazenar em uma lista
Depois criar duas novas listas separando entre impares e pares, e por final
apresentar na tela
'''
lista = []
listaPar = list()
listaImpa = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar?(SIM/NAO) ').upper())
    if resposta in 'NAO':
        break

for index, valor in enumerate(lista):
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpa.append(valor)

lista.sort()
print(f'Lista com os valores originais {lista}')
print(f'Lista com os valores pares{listaPar}')
print(f'Lista com os valores impares {listaImpa}')