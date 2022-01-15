#Crie um programa que peça para digitar 7 vezes e armaze em uma lista.
#Cadastre em uma única lista e separe entre pares e impar, além de apresentar
# de forma crescente

listaValor = [[],[]]

for registro in range(1,8):
    numero = int(input(f"Digite o {registro}º valor: "))
    if numero % 2  == 0:
        listaValor[0].append(numero)
    else:
        listaValor[1].append(numero)

listaValor[0].sort()
listaValor[1].sort()
print(f"Lista de valores Pares {listaValor[0]}")
print(f"Lista dos valores Impares {listaValor[1]}")
print(f"Lista completa: {listaValor}")
