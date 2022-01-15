# Leia peso de 5 pessoas e mostre qual foi o maior e menor peso.

maior = 0
menor = 0

for c in range(1,6):
    pesoUsuario = int(input('Valor da {}º pessoa '.format(c)))
    if c == 1:
        maior = pesoUsuario
        menor = pesoUsuario
    if pesoUsuario > maior:
        maior = pesoUsuario
    if pesoUsuario < menor:
        menor = pesoUsuario

print('''
Pessoa com maior peso é de {} Kg
Pessoa com menor peso é de {} Kg
'''.format(maior, menor))