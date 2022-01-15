'''Crie um programa que leia o nome e duas notas de vários alunos e guarde em uma
lista composta. No final mostre um boletim contendo a média de cada um e permita que
o usuário possa mostrar as notas de cada aluno individualmente.
'''

ficha = list()

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Digite a nota 1: '))
    nota2 = int(input('Digite a nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    respota = str(input('Deseja continuar? S/N '))
    if respota in 'Nn':
        break

print(f'{"N":<4}{"NOME":<8}{"MÉDIA":>8}')
for index, aluno in enumerate(ficha):
    print(f'{index:<4}{aluno[0]:<8}{aluno[2]:>8}')

while True:
    opcao = int(input('Qual aluno você deseja ver as notas?(Digite 999 para sair.): '))
    if opcao == 999:
        print("Programa finalizado.")
        break
    if opcao <= len(ficha) - 1:
        print(f'Nota de {ficha[opcao][0]} são {ficha[opcao][1]}')