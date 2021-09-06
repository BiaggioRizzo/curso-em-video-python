# Crie um programa que leia um número Real(float) qualquer pelo teclado e mostre na tela a sua porção inteira

# import math       - import generalista
#Import da função especifica
from math import trunc

numero = float(input('Digite um número real: '))
print('Porção inteiro é {}'.format(trunc(numero)))
