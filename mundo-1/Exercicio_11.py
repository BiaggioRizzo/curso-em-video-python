# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessário para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Digite a lagura da parede: '))
comprimento = float(input('Digite o comprimedo da parede: '))

area = largura * comprimento
tinta = area/2

print('A largura da parede é {} e o comprimento é de {}, com a área total de {}m².'. format(largura, comprimento, area))
print('Necessário utilizar {} litros de tintas, para pintar a parede'.format(tinta))
