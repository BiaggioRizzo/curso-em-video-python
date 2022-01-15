#Leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora de se alista ou se já passou o tempo do alistamento.
#Apresentar o tempo que falta ou que passou

import datetime

esseAno = datetime.date.today().year
anoNascimento = int(input('digite seu ano de nascimento: '))
idade = esseAno - anoNascimento

if idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para se alistar.'.format(saldo))
    ano = esseAno + saldo
    print('Você vai se apresentar no ano {}.'.format(ano))
elif idade == 18:
    print('Você precisa se alistar urgente!')
else:
    saldo = idade - 18
    print('Já passaram {} anos para se alistar.' .format(saldo))
    ano = esseAno - saldo
    print('Você se apresentou no ano {}.'.format(ano))
