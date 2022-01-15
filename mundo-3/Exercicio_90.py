#Faça um programa que leia nome e média de um aluno e guarde também a situação em um 
#dicionário. No final, mostrer o conteúdo da estrutura na tela

dicionario = dict()
dicionario['Nome'] = str(input("Nome: "))
dicionario['Media'] = float(input(f"Média de {dicionario['Nome']}: "))
if dicionario['Media'] >= 7:
    dicionario['Situacao'] = 'Aprovado'
else:
    dicionario['Situacao'] = 'Reprovado'

for keys, values in dicionario.items():
    print(f'{keys} é igual {values}')