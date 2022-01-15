# leia a altura e o peso de uma pessoa e calcule o IMC.
# Abaixo de 18.5: Abaixo do peso |entre 18.5 a 25: ideal | 25 até 30 : sobrepeso | 30 até 40 obesidade |
# Acima obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura * altura) #ou altura ** 2  | mesma coisa
if imc < 18.5:
    print('Seu imc {:.2f} indica abaixo do peso.'.format(imc))
elif imc < 25:  #ou então 18.5 <= imc < 25:
    print('Seu imc {:.2f} indica ideial.'.format(imc))
elif imc < 30:
    print('Seu imc {:.2f} indica sobrepeso'.format(imc))
elif imc < 40:
    print('Seu imc {:.2f} indica Obesidade'.format(imc))
else:
    print('Seu imc {:.2f} indica Obesidade mórbida'.format(imc))
