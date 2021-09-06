#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Digite o seu salário: R$ '))
aumento = salario * 115 / 100       # Ou aumento = salario + (salario * 15 / 100)

print('Seu salário é de R${} e teve um aumento de 15%.\nSeu salário agora é de R${:.2f}' .format(salario, aumento))

