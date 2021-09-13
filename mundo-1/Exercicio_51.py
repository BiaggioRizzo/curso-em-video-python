# Leia primeiro termo e a razao de uma PA e mostre os 10 primeiros
primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite o número da razão: '))
decimo = primeiro + (10 + 1 ) * razao

for c in range(primeiro, decimo, razao):
    print ('{}'.format(c), end= ' ')

    