#Ler seis numeros e some os números pares descartando os números impares

soma = 0
contador = 0 
contadorValido = 0

for c in range(0,6):
    contador += 1
    usuario = int(input('Digite um valor: '))
    if usuario % 2 == 0:
        soma += usuario
        contadorValido += 1

print('Nos {} números digitados, apenas {} foram validos com o somatorio de {}'.format(contador, contadorValido, soma))