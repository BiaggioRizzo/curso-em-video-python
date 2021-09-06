#escreva um programa que faça o computador escolher um número de 0 a 5 e o usuário descobrir o número que o computador escolheu
# caso acerte o apresente a mensagem usuário venceu ou perdeu

from random import randint

sorteio = randint(0, 5)
numero = int(input('Digite um número de 0 a 5: '))

if numero == sorteio:
    print('Acertou')
else:
    print('Tente novamente')

#if simplificado
#print('Acertou' if numero == sorteio else 'Tente novamente')

print('Número sorteado foi {}' .format(sorteio))

