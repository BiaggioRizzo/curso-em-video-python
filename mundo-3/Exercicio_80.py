#Usuário digite 5 vezes e ordene já na ordem sem utiliza o sort. No final mostra a ordem
valores = []

for lista in range(0,5):
    numero=(int(input("Digite o valor: ")))
    if lista == 0 or numero > valores[-1]:
        valores.append(numero)
        print('Número adicionado no final da lista.')
    else:
        posicao = 0
        while posicao < len(valores):     #Vai percorrer todas as posições da lista
            if numero <= valores[posicao]: #Vai verificar se o valor é menor ou igual na posição lista
                valores.insert(posicao,numero)
                print(f'Número adicionado na posição {posicao} da lista.')
                break
            posicao += 1

print(valores)