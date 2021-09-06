#Calcule o valor a ser pago por um produto, considerando o seu preço normal e condições de pagamento:
#à vista dinheiro/cheque 10% de desconto | à vista no cartão: 5% de desconto | em até 2x no cartão preço normal
#3x ou mais no cartão: 20% de juros

produto = float(input('Digite o preço do produto: R$'))
pagamento = int(input('''Digite a forma de pagamento:'
[1] À vista dinheiro
[2] À cheque
[3] Cartão de crédito
Digite: '''))

if pagamento == 1 or pagamento == 2:
    pagar = produto - produto * (10 / 100)
    print('Valor a pagar é R${:.2f}'.format(pagar))
elif pagamento == 3:
    parcelas = int(input('Quantas parcelas deseja fazer? '))
    if parcelas == 1:
        pagar = produto - produto * (5 / 100)
        print('Valor a pagar é R${:.2f}'.format(pagar))
    elif parcelas == 2:
        print('Valor a pagar é R${:.2f}'.format(produto))
    else:
        pagar = produto * (120 / 100)
        print('Valor a pagar é R${:.2f}'.format(pagar))
else:
    print('Opção invalida.')
