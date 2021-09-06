name = input('Digite algo: ')
print('O tipo primitivo desse valor é : ', type(name))
print('Só tem espaços? ', name.isspace())
print('É número? ', name.isalnum())
print('É alfanumérico? ', name.isalpha())
print('É tudo minusculo? ', name.islower())
print('É tudo maisculo? ', name.isupper())
#capitalizado é quando tem minusculo e maisculo na string
print('Está capitalizada? ', name.istitle())
