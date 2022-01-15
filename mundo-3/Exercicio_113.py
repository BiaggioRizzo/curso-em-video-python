#Reescreva a função leiaInt() realizada no exercicio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#A proveite e crie também uma função leiaFloat() Com a mesma funcionalidade.
def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except KeyboardInterrupt:
            print("Programa interrompido.")
            return 0
        except (TypeError, ValueError):
            print("Digite um valor interio válido. ")
        else:
            return numero


def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (TypeError, ValueError):
            print("Digite um número real!")
        except KeyboardInterrupt:
            print("Programa interrompido.")
            return 0
        else: 
            return numero


def leiaNumero(mensagem):
    while True:
        try:
           numero = float(input(mensagem))
           if numero % 1 == 0:
               numero = int(numero)
        except KeyboardInterrupt:
            print("Programa interrompido.")
            return 0
        except (TypeError, ValueError):
            print(f"Digite um valor inteiro ou real válido. ")
        else:
            return numero


#respostaInt = leiaInt("Digite um número inteiro: ")
#rint(f'Resposta retornada foi: {respostaInt}')

#respostaFloat = leiaFloat("Digite um número real: ")
#print(f'Resposta retornada foi: {respostaFloat}')

respostaNumero = leiaNumero("Digite um número: ")
print(f'Resposta retornada foi: {respostaNumero}')