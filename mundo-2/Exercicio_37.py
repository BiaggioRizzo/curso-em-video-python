#Escreva um programa que leia um número inteiro qualquer e peça para usuário escolher qual será a base de conversão:
# 1 para binário | 2 para octal | 3 para hexadecimal

print('Base de conversão:', end='')#\n[1] Binário\n[2] Octal\n[3] Hexadecimal') ou
print(''' 
[1] Binário
[2] Octal
[3] Hexadecimal''')

escolha = int(input('\nDigite a base de conversão desejada: '))
numero = int(input('Digite um número inteiro: '))

if escolha == 1:
    print('{} convertido para binário é igual a {}.'.format(numero, bin(numero)[2:]))   #[2:] esta eliminando os dois primeiros caracter
elif escolha == 2:                                                                      #que aparece para representar as bases.
    print('{} convertido para octal é igual a {}.'.format(numero, oct(numero)[2:]))     #É o fatiamento de strings
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Erro no dígito.')
