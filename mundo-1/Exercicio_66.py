#Leia vários números inteiros e só ira para quando digitar 999. No final mostre a quantidade total de números digitadas e a soma desses valores, desconsiderando a flag
#Utilize while true 
quantidadeTotal = somaTotal = numero = 0

while True:
    numero = int(input('[999 - stop] - Digite um valor: '))
    if numero == 999:
        break
    quantidadeTotal += 1
    somaTotal += numero

print(f'Soma de {quantidadeTotal} valores é igual a {somaTotal}')