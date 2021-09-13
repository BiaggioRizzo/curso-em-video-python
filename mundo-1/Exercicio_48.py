# Some todos os números pares que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
count = 0

for c in range(1,500,2):
    if c % 3 == 0:
        soma += c
        count += 1

print('A soma de todos os {} números deram o resultado de {}'.format(count,soma))