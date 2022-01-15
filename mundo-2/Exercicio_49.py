# Tabua utilizando laço de repetição for

usuario = int(input("Digite valor da tabuada: "))

for c in range(0,11):
    resultado = usuario * c
    print('{}x{:2} = {}' .format(usuario, c, resultado))
    
