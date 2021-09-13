# Leia um número inteiro e verifica se é ou não um número primo. 

numero = int(input('Digite um número: '))
total = 0

for c in range (1, numero + 1):
    if numero % c == 0 :
        print('\033[33m', end='')
        total += total
    else:
        print('\033[31m', end='')
    print('{}' .format(c), end='')

if total == 2:
    print('O número é primo!')
else:
    print('O número não é primo.')