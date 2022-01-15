#Criar uma lista e depois mostrar quantos números foram digitados, ordenar de forma
#decrescente e verificar se o número 5 está incluso na lista.

lista = []

while True:
    lista.append(int(input("Digite o Valor: ")))
    condicao = (str(input("Deseja continuar?(SIM/NAO): ")).upper())
    if condicao in 'NAO':
        break 

if 5 in lista:
    print("Contém o número 5 na lista.")
else:
    print('Não contém o número 5 na lista.')

print(f'A quantidade de números digitados foram {len(lista)}')
lista.sort(reverse=True)
print(lista)