#Aprimore o exercicio 86.
''' Some os valore pares digitados
    Some os valores da terceira coluna
    o maior valor da segunda linha
'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
somaValorPar = int()
somaTerceiraColuna = int()
maiorValor = 0


for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]= int(input(f'Digite um valor para posição [{linha},{coluna}]: '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        if matriz[linha][coluna] % 2 == 0:
            somaValorPar += matriz[linha][coluna]
    print()
        
print(f'Soma de todos valore pares foi de {somaValorPar}')


for linha in range(0,3):
    somaTerceiraColuna += matriz[linha][2]

print(f'A soma de todos os valores da terceira coluna foi de {somaTerceiraColuna}')

for coluna in range(0,3):
    if maiorValor == 0:
        maiorValor += matriz[1][coluna]
    elif maiorValor < matriz[1][coluna]:
        maiorValor = matriz[1][coluna]

print(f'O maior valor registrado na segunda linha foi de {maiorValor}')