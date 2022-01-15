# Leia sexo e aceite só valores 'M' ou 'F', caso esteja errado, mande escrever novamente

sexo = str(input('Digite o sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite novamente: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso.'.format(sexo))