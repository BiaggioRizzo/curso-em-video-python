# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input('Digite a temperatura em Graus Celsius:'))
fahrenheit = ((celsius * 9) / 5) + 32

print('Temperatura em Graus Fahrenheit é de {:.2f}°F' .format(fahrenheit))
