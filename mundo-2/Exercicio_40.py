#Leia duas notas de um aluno e calcule sua média.
#Caso seja abaixo de 5 reprovado, entre 5 a 6.9 recuperação e acima de 7 aprovado

notaUm = float(input('Digite sua primeira nota: '))
notaDois = float(input('Digite a sua segunda nota: '))

media = (notaUm + notaDois) / 2
if media < 5:
    print('Você foi reprovado.')
elif media >= 5 and media <= 6.9: # ou elif  7 > media >= 5
    print('Recuperação:')
else:
    print('Aprovado!')

print(media)