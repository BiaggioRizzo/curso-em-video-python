#Programa leia nome e preço de vários produtos, no final soma o total de gasto
#motrar quantos produtos foram mais que 1000 reais e mostra o nome do mais barato
totalGasto = precoProdutoCaro = 0
produtoBarato = ' '

while True:
    nomeProduto = str(input("Digite o nome do produto: ")).strip()
    preco = int(input('Digite o preço do produto: '))
    if preco >= 1000:
        precoProdutoCaro += 1
    tempPreco = 0
    if tempPreco < preco:
        produtoBarato = nomeProduto
    totalGasto += preco
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    
    if resposta == 'N':
        break
print(f'''
Foram no total de {precoProdutoCaro} produtos acima de R$1000,00.
O produto mais barato é {produtoBarato}.
Total gasto = {totalGasto}
''')