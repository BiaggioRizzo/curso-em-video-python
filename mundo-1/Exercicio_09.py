#Exercício de Tabuada

numero = int(input('Digite o numero da tabuada: '))

print('Tabela da tabuada de {}:'.format(numero))
print('-' * 15)

for i in range(1, 11):

    print('{} x {} = {}'.format(numero, i, (numero * i)))

print('-' * 15)