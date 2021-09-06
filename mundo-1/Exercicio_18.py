# Faça um programa que leia um ângulo qualquer e mostre na tela o valro do seno, cosseno e tangente desse ângulo

import math

angulo = int(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O ângulo {} tem o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cos, tang))

