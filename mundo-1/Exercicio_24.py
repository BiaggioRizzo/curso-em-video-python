#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Digite nome de uma cidade: ')).strip()

cidade = cidade.split()
print('SANTO' in cidade[0].upper())

# Outro método de fazer:
# print(cid[:5].upper() == 'SANTO')