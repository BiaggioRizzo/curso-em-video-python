'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salario.
Calcule e acescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

import datetime

date = datetime.date.today().year
registro = dict()
tempoMinimoAposentadoria = 35

registro['nome'] = str(input('Digite seu nome: '))
registro['idade'] = date - int(input('Digite o ano de nascimento: '))
registro['carteiraTrabalho'] = int(input('Digite o número da carteira de trabalho (0 caso não tenha): '))
if registro['carteiraTrabalho'] != 0:
    registro['anoContratacao'] = int(input('Digite ano da contratação: '))
    registro['salario'] = float(input('Digite o seu salário: '))
    registro['aposentadoria'] = registro['idade'] + ((registro['anoContratacao'] + tempoMinimoAposentadoria) - datetime.date.today().year)

print()
print('-'*20)
for keys, values in registro.items():
    print(f'{keys} = {values}')
