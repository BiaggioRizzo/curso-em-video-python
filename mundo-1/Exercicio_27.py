#Faça um programa que leia o nome completo de uma pessoa, monstrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
print('Prazer em conhece-lo {}'.format(nome))
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

#raciocinio do programa:
#método split vai dividir a frase e cada palavra torna-se uma posição na lista
#dessa maneira a método  len vai contar a quantidade total da lista, porém deve colocar -1 pelo motivo que a lista começa
#na posição 0