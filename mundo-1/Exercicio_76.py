#Crie um programa com nome de produtos e seus respectivos preços. no final mostre uma lista com formato de tabular

listagem = ('lápis', 1.80,
            'caneta', 3,
            'borracha', 2,
            'apontador',1.5)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f"R${listagem[posicao]:>5.2f}")
    
