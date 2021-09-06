#Crie um programa que leia um nome completo de uma Pessoa e mostre:
# * O nome com todas as letras maiúsculas
# * O nome com todas as letras minúsculas
# * Quantas letras ao todo (sem considerar espaços)
# * Quantas letras tem o primeiro nome

name = str(input('Digite seu nome completo: ')).strip()     #Remove os espaços no começo e no final
# letras maiúsculas
print(name.upper())
# letras minúsculas
print(name.lower())

#Removo os espaços em branco e conto a quantidade de letras
print(len(name.replace(' ', '')))

# Quantas letras tem o primeiro nome
name = name.split()
print(len(name[0]))
#.format(name.find(' '))) vai contar a quantidades até o primeiro espaço
