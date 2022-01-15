#Cria uma função chamada leiaInt(), que vai funcionar de forma semelhante à função input(),só que vai fazer a validação
#aceitando apenas valóres numericos. Ele só vai parar quando receber um valor inteiro.

def leiaInt(mensagem):
    valido = False
    valor = 0
    while True:
        numero = str(input(mensagem))   # Essa linha faz com que consiga replicar o estado de input
        if numero.isnumeric():
            valor = int(numero)
            valido = True
        else:
            print("\033[0;31mERROR! Digite um número inteiro novamente.\033[m")
        if valido:
            break
    return valor    


n = leiaInt("Digite um número: ")
print(n)