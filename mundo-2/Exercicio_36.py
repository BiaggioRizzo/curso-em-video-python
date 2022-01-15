#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

salario = float(input('Digite o valor do seu salário: R$'))
casa = float(input('Qual o valor da casa? R$'))
tempo = int(input(('Quantos anos pretende pagar? ')))
parcelas = casa / (tempo * 12)
print('Valor de cada parcela sera de R${:.2f}'.format(parcelas))
minimo = salario * (130 / 100)

if parcelas >= minimo:
    print('Não foi aprovado para o empréstimo.')
else:
    print('Foi aprovado para o empréstimo.')