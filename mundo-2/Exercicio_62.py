#Melhore o exercicio 61 e pergunte quantos termos quer mostrar a mais, caso digite 0 finalize o programa

print("Descobrindo PA")
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
quantidade = 1

''' Meu desenvolvimento 
while quantidade > 0 :
    print('{}'.format(termo), end='')
    print(' -> ' if quantidade > 1 else ' - Pausa ', end='')
    termo += razao
    quantidade -= 1
    if quantidade == 0:     #Funcionou, porém não é das melhores práticas
       quantidade = int(input('\nQuantos termos deseja mostrar a mais? '))
'''
acrescimo = 10
total = 0
while acrescimo != 0:
    total = total + acrescimo
    while quantidade < total :
        print('{} -> '.format(termo), end='')
        termo += razao
        quantidade += 1
    print('Pausa')
    acrescimo = int(input('Quantos termos a mais deseja? '))
