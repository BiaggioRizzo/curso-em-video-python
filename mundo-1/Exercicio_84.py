''' Faça um programa que leia vários nomes e peso das pessoas e armazene em
uma lista. No final mostre Quantas pessoas foram cadastradas, lista com as pessoas
mais pesadas e uma lista com as pessoas mais leve 
'''

ficha = list()
dados = []
maior = menor = 0

while True:
    dados.append(str(input("Digite seu nome: ")))
    dados.append(int(input("Digite o seu peso: ")))
    if len(ficha) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados [1] < menor:

            menor = dados[1]
    ficha.append(dados[:])
    dados.clear()
    condicao = str(input("Deseja continuar?(S/N)")).upper()
    if condicao != "S":
        break


print(f"Quantidade de pessoas cadastradas foram {len(ficha)}")
print(f'O maior peso registrado foi {maior} kg. ', end='')
for pessoa in ficha:
    if pessoa[1] == maior:
        print(f"Nome da(s) pessoa(s): {pessoa[0]}")

print(f'O menor peso registrado foi {menor} kg. ', end='')
for pessoa in ficha:
    if pessoa[1] == menor:
        print(f"Nome da(s) pessoa(s): {pessoa[0]}",end='')