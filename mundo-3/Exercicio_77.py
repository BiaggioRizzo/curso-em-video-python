#crie um programa que tenha uma tupla com varias palavras e mostrar quais sao as vogais dessa palavra

palavras = ('aprender','estudar','programar','desafio','trabalho')

for sentenca in palavras:
    print(f'\nNa palavra {sentenca.upper()} ', end='')
    for letra in sentenca:
        if letra.lower() in 'aeiou':
            print(letra, end='')
