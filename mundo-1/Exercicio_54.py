# leia o ano de nascimento de 7 pessoas e no final mostre quantas são maiores de idades e menores de idades;

from datetime import date

anoAtual = date.today().year
maior = 0
menor = 0

for c in range(1,8):
    anoNasc = int(input('Em que ano a {}º pessoa nasceu: '.format(c)))
    if anoAtual - anoNasc > 18 :
        maior += 1
    else:
        menor += 1

if maior > 1 and menor > 1:
    print('Exitem {} pessoas maiores de idade e {} menores de idade'.format(maior,menor))
elif maior > 1 and menor == 1:
    print('Exitem {} pessoas maiores de idade e {} menor de idade'.format(maior,menor))
else:
    print('Exite {} pessoa maior de idade e {} menores de idade'.format(maior,menor))
