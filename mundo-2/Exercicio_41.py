#Leia o ano de nascimento e um atleta e mostre sua categoria de acordo com idade
# até 9 = mirim | até 14 = infantil | até 19 = Junior | até 25 senior | acima master

from datetime import date
anoAtual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - nascimento
print ('O atelta tem {} anos.'.format(idade))
if idade < 9:
    print('Sua classificação: Mirim')
elif 14 >= idade > 9:
    print('Sua classificação: Infantil')
elif idade <=19:
    print('Sua classificação: Junior')
elif idade <= 25:
    print('Sua classificação: Senior')
else:
    print('Sua classificação: Master')