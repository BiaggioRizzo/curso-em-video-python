# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

produto = float(input('Preço do produto: '))
desconto = produto - (produto * (5/100))

print('Valor do produto: R${}\nValor do produto com desconto de 5% é: R${:.2f}'.format(produto, desconto))
