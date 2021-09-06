#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0.15 por km rodados.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))

diasAlugados = 60
kmPercorridos = 0.15
pago = (dias * diasAlugados) + (km * kmPercorridos)

print('Valor a ser pago é {:.2f}'.format(pago))



