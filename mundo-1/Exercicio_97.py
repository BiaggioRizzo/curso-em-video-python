#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptavél.

def escreva(mensagem):
    tamanho = len(mensagem) + 2
    print('~'*tamanho)
    print(f" {mensagem}")
    print('~'*tamanho)

   
escreva("Olá, mundo!")