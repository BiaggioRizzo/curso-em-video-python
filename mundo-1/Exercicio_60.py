#Leia um número inteiro e mostre o seu fatorial utilizando while

numero = int(input('Digite um número: '))
resultado = 1

print('Calculando {}! = '.format(numero), end='')
while numero > 0:
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' = {}'.format(resultado), end='')
    resultado *= numero
    numero -= 1