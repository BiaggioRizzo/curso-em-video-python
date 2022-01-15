#Leia vários numeros inteiros e que mostre no final a media entre todos os números, qual foi o maior e o meno. Verifique se o usuário deseja ou não continuar.

maior = menor = quantidade = somaTotal = numero = 0
decision = ''

while decision in 'S':
    numero = int(input('Digite o número: '))
    quantidade += 1
    somaTotal += numero
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    decision = str(input('Deseja continuar(S/N)? ' )).strip().upper()[0]

media = somaTotal/quantidade
print('''
Digitaram {} número(s).
O maior número foi {}.
O menor número foi {}.
A média dos números foram {}
'''.format(quantidade,maior,menor,media))