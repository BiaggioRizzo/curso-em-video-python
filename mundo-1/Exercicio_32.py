#Leia um ano qualquer e mostre se é um ano Bissexto.

from datetime import date

ano = int(input('Digite o ano que deseja analisar.\nCaso deseja verificar esse ano digite o número "0": '))

#if ano == 0:
#    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    if ano == 0:
        ano = date.today().year
    print('O ano {} é bissexto'.format(ano))

else:
    print('O ano {} não é bissexto'.format(ano))
