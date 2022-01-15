#Usuário digite vários valores numéricos e coloque dentro de uma lista.
# Caso o número exista, não sera adicionado, no final serão exibidos os valores únicos em ordem crescente.

#Feito por mim:
valores = []
condicao = 'SIM'

while (condicao == 'SIM'):
    valor = int(input("Digite um valor: "))
    if valor in valores:
        print("Número já foi digitado")
    else:
        valores.append(valor)
    condicao = str(input('Deseja continuar? ')).upper()

print(f'Valores foram {valores.sort}', end='')

#Feito pelo professor:

numeros = list()

while True:
    numeroDigitado = int(input('Digite um valor: '))
    if numeroDigitado not in numeros:
        numeros.append(numeroDigitado)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado!')
    resposta = str(input('Deseja continuar?'))
    if resposta in 'Nn':
        break


print(f'Os números digitados foram: {numeros.sort}')
