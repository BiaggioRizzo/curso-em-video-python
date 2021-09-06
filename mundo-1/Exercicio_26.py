#Faça um programa que leia uma frase pelo teclado e mostre:
#   Quantos vezes aparece a letra "A"
#   Em que posição ela aparece a primeira vez.
#   Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" apareceu no total de {} vez.'.format(frase.lower().count('a')))
print('Primeira vez que aparece é na {}° posição'.format(frase.upper().find('A')+1))
print('Última vez que aparece é na {}° posição'.format(frase.upper().rfind('A')+1))
#rfind começa pelo lado direito. 