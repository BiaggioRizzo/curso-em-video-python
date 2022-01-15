''' Faça uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem
Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1   | B) De 10 até 0, de 2 em 2     | C) Uma contagem personalizada.
'''
from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    contagem = inicio
    if inicio < fim:
        while contagem <= fim:
            print(f'{contagem}', end=' ', flush=True)
            contagem += passo
            sleep(0.2)
        print()
    elif inicio> fim:
        while contagem >= fim:
            print(f'{contagem}', end=' ', flush=True)     #flush=True ele não vai ligar o buff da tela, dessa forma vai funcionar o delay de cada número aparecendo.
            sleep(0.2)
            contagem -= passo
        print()


contador(1,10,1)
contador(10,0,2)

print('Digite o seu contador:')
start = int(input("Inicio: "))
end = int(input('Fim: '))
step = int(input('Passo: '))
contador(start, end, step)