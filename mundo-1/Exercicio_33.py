#Faça um programa que leia três números e mostre qual é o maior valor e qual é o menor.
#Existe uma função que descobre o maior e o menor valor.

numeroUm = int(input('Digite o primeiro número: '))
numeroDois = int(input('Digite o segundo número: '))
numeroTres = int(input('Digite o terceiro número: '))

menor = numeroUm
if numeroDois < numeroUm and numeroDois < numeroTres:
    menor = numeroDois
if numeroTres < numeroDois and numeroTres < numeroUm:
    menor = numeroTres

maior = numeroUm
if numeroDois > numeroUm and numeroDois > numeroTres:
    maior = numeroDois
if numeroTres > numeroDois and numeroTres > numeroUm:
    maior = numeroTres

print('Maior número {} e o menor número {}.'.format(maior, menor))

#Outra maneira de resolver:
maximo = max(numeroUm, numeroDois, numeroTres)
minimo = min(numeroUm, numeroDois, numeroTres)
print('Maior número {} e o menor número {}.'.format(maximo, minimo))