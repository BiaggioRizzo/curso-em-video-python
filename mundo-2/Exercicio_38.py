#escreva um programa que leia dois números interios e compare-os, mostrando na tela uma mensagem:
#   O primeiro valor é maior
#   O Segundo valor é maior
#   Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O primeiro valor ({}) é maior que o segundo valor ({}).'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor ({}) é maior que o primeiro valor ({}).'.format(n2,n1))
else:
    print('Não existe valor maior, os dois valores são iguais.')
