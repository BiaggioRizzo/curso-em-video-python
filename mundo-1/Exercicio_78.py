#Leia 5 valores e guarde em uma lista e no final mostre qual foi o maior e menor e suas respectivas posições na lista.

valores = []
maior = 0 
menor = 0
for lista in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if lista == 0:
        maior = menor = valores[lista]
    else:
        if valores[lista] > maior:
            maior = valores[lista]
        if valores[lista] < menor:
            menor = valores[lista]
#enumerate ele pega tanto a chave quanto os valores
print(f'O maior valor foi {maior}, digitado nas posições', end='')
for chave, valor in enumerate(valores):
    if valor == maior:
        print(f'\n{chave}...', end='')
print(f'\nO menor valor foi {menor}, digitado nas posições', end='')
for chave, valor in enumerate(valores):
    if valor == menor:
        print(f'\n{chave}...', end='')