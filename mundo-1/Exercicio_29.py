#Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
# multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite velocidade atual do carro: '))

if velocidade <= 80:
    print('\033[33mTenha uma boa viagem! Dirija com segurança!')
else:
    multa = (velocidade - 80) * 7.00
    print('\33[31mVocê ultrapassou o limite permitido, você deve pagar a MULTA de R${:.2f}' .format(multa))
