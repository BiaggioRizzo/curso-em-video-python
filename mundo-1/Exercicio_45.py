#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Vamos jogar Jokenpô!
Suas opções são:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual é sua escolha? '))

if computador == jogador:
    print('-=' * 12)
    print('\tEmpate')
elif computador < jogador:
    print('-=' * 12)
    print('\tJogador Ganhou')
else:
    print('-=' * 12)
    print('\tJogador perdeu')

print('-=' * 12)
print('Computador jogou {}' .format(itens[computador]))
print('Você jogou {}' .format(itens[jogador]))
print('-=' * 12)
