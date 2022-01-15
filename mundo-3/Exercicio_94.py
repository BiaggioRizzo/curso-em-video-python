''' Crie um programa que leia nome, sexo e idade de várias pessoas e guarde cada um
em um dicionário e todos os dicionário em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas | B) A média de idade | C) Lista de todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
'''

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa ['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Resposta apenas S ou N.')
    if resposta == 'N':
        break

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma /len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastras foram ', end='')
for pessoa in galera:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}', end=', ')
    
print()
print('D) Lista das pessoas que estão acima da média: ')
for pessoa in galera:
    if pessoa['idade'] >= media:
        print(' ')
        for keys, values in pessoa.items():
            print(f'{keys} = {values}', end='   ')
        print()

print('<< Programa finalizado >>')