#Faça um programa que tenha uma função chamada area(), que receba as dimensoes de um terreno retangular
# (largura e comprimento ) e mostre a área do terreno.

def area(largura, comprimento):
    areaTerreno = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {areaTerreno}')


largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura,comprimento)
