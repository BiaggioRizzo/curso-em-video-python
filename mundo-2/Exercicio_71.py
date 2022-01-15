#Crie um caixa eletrônico, onde usuário digite valor inteiro de saque e mostre
#quantas cédulas deve ser entregue. (OBS: 50, 20, 10, 1)

valor50 = valor20 = valor10 = valor1 = 0
valor = int(input('Digite valor: '))
total = valor
#Resposta curso em video. 

cedula = 50
totalCedula = 0
while True: 
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f"Total de {totalCedula} cédulas de R${cedula}.")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break

