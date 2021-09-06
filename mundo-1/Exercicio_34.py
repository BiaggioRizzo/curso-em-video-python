#Escreva um programa que pergunte o salário de um funcionário e calcule o valro do seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: R$'))

aumento = salario * 110 / 100 if salario >= 1250 else salario * 115 / 100

print('O salário antigo era de R${}, com o aumento salarial ficou R${}' .format(salario, aumento))
