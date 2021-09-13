# Leia dois valores e mostre um meno com as operações 
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('''Opções disponíveis:
            [1] - Somar
            [2] - Multiplicar
            [3] - maior
            [4] - Selecionar novos números
            [5] - Sair do programa''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1 :
        resultado = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1,n2,resultado))
    elif opcao == 2 :
        resultado = n1 * n2
        print('A multiplicação entre {} * {} = {}'.format(n1,n2,resultado))
    elif opcao == 3:
        if n1 > n2:
            print("Maior número é {}.".format(n1))
        elif n2 > n1:
            print('Maior número é {}.'.format(n2))
        else:
            print('Ambos tem o mesmo valor.')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

print('Fim')
