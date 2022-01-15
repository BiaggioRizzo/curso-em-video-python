#Leia um número e mostre a tabuada. O programa se encerra quando número for negativo

while True:
    numero = int(input("Digite o número: "))
    if numero < 0 :
        break
    for c in range(1,11):
        print(f"{numero} x {c} = {numero*c}")
