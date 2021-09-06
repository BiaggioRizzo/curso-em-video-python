#Exercício dobro, triplo e raiz de um número:

import math

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5
# Utilizando método da biblioteca math
#raiz = math.sqrt(numero)
print('Dobro do valor: {}\nTriplo do valor: {}\nRaiz do valor {:.3f}'.format(dobro, triplo, raiz))
