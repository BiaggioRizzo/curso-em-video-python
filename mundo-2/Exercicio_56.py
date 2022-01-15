# Leia nome, idade e sexo de 4 pessoas e mostre qual a idade média do grupo, homem mais velho e quantas mulheres tem menos de 20 anos

menorIdade = 0
maiorIdade = 0
oldMan = ''
mediaIdade = 0

for pessoa in range(1,5):
    print('{}º Pessoa: '.format(pessoa))
    nome = str(input('Digite o seu nome: '))
    sexo = str(input('Digite seu sexo (F/M): ')).upper()
    idade = int(input('Digite sua idade: '))

    if sexo == 'F' and idade <= 20:
        menorIdade += 1
    if sexo == 'M' and idade > maiorIdade:
        oldMan = nome

    mediaIdade += idade

mediaIdade = mediaIdade/4
print('''
A média de idade do grupo é {} anos.
O homem mais velho chama-se {}.
Existe {} mulheres menores que 20 anos.'''.format(mediaIdade,oldMan,menorIdade))