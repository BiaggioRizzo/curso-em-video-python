#Leia vários numeros inteiros e só ira para quando digitar 999. No final mostre a quantidade total de números digitadas e a soma desses valores, desconsiderando a flag

quantidadeTotal = somaTotal = numero = 0

numero = int(input('[999 - stop] - Digite um valor: '))
while numero != 999:
    quantidadeTotal += 1
    somaTotal += numero
    numero = int(input('[999 - stop] - Digite um valor: '))

print('Soma de {} valores é igual a {}'.format(quantidadeTotal,somaTotal))