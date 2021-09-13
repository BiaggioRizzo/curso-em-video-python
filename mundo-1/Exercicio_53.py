#Crie uma frase e diga se ela é um palíndrome, desconsidere os espaços.

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
print(palavras)
inverso = ''

for letra in range(len(juntar) -1 , -1 ,-1):
    print(juntar[letra])
    inverso += juntar[letra]

if inverso == juntar:
    print('É palíndrome!')
else:
    print('Não é palíndrome.')
