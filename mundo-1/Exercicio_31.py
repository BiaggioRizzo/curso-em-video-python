#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, combrando R$0,50 por km para viagens até 200Km e R$0,45 para viagens mais longas

distancia = float(input('Digite a distância da viagem: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# ou
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Valor da passagem é R${:.2f}'.format(preco))

