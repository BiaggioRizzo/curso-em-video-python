''' Crie um programa que digite uma expressão e verifica se está com os 
parênteses abertos e fechados na ordem correta.
'''

expressao = str(input('Digite uma expressão:'))
pilha = list()

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha)>0:
            pilha.pop #removo o último elemento
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("Sua expressão está correta!")
else:
    print("Sua expressão está errada! \nTente novamente.")
    
