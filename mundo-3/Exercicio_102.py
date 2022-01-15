'''Crie uma função chamada fatorial() que receba dois parâmetros: o primeiro indica o número e o segundo 
chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial.
'''

def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :parm show: (Opcional) Mostra o desenvolvimento da conta, caso esteja habilitado.
    :return: Resultado do fatorial do número.
    """
    from time import sleep
    contador = 1
    for numero in range(numero, 0, -1):
        if show == True: # if show:    <-- Possibilidade
            print(f'{numero}',end='',flush=True)
            if numero > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
            sleep(0.2)
        contador *= numero
    return contador


print(fatorial(6,True))
help(fatorial)