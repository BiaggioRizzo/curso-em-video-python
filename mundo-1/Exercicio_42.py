#Refaça o exercício 35, acrescentando o recurso de mostra que tipo de triângulo será formado:
# Equilátero = todos os lados iguais | Isósceles: dois lados iguais  | Escaleno: todos os lados diferentes

r1 = float(input('Digite o primeiro segmento'))
r2 = float(input('Digite o segundo segmento'))
r3 = float(input('Digite o terceiro segmento'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos podem forma um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('As medidas passadas não podem forma um triângulo!')
    exit(0)

