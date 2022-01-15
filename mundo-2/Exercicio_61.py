# Refazer desafio 51 utilizando while. Leia o termo e a razao e uma PA e mostre os 10 primeiros

print("Descobrindo PA")
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
quantidade = 10

while quantidade > 0 :
    print('{}'.format(termo), end='')
    print(' -> ' if quantidade > 1 else ' - Fim ',end='')
    termo += razao
    quantidade -= 1