# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math

catOposto = float(input('Digite o cateto oposto: '))
catAdjacente = float(input('Digite o cateto adjacente:' ))
hipotenusa = math.hypot(catOposto,catAdjacente)
# outra maneira de fazer é hipotenusa = (catOposto ** 2 + catAdjacente ** 2 ) ** (1/2)
print('Comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
