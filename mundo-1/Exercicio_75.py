#Leia 4 valores e armazene em uma tupla.
#Mostre quantas vezes apareceu valor 9, qual posição do número 3 apareceu e quais numeros foram pares

valores= (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))
  
print(f'Os números digitados foram: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na posição {valores.index(3)+1} ')
else:
    print('Não foi digitado nenhum valor 3')

print('Os valores pares foram: ',end= '')
for n in valores:
    if n % 2 == 0:
        print(n, end= ' ')
