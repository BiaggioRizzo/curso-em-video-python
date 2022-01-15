#Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digita o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM' o programa se encerrará | Utilize cores
cores = (
    '\033[m',           # 0 - sem cor
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30',        # 6 - branco
)
'''
Minha resolução: 
def manual():
    global cores
    comando = ''
    while comando != 'Fim':
        print('~' * 30, cores[1])
        print(f'{"SISTEMA DE AJUDA PyHelp":^30}',cores[1])
        print('~' * 30,cores[1])
        comando = str(input("Função ou Biblioteca: "))
        print('~' * 34, cores[3])
        print(f'Acessando o manual do comando "{comando}"', cores[3])
        print('~' * 34, cores[3])
        print('~' * 30, cores[5])
        print(help(comando),cores[5])
        print('~' * 30, cores[5])


manual()
'''
# Solução do professor:
def ajuda (comando):
    titulo(f'Acessando o manual do comando {comando}',3)
    print(cores[6],end='')
    help(comando)
    print(cores[0],end='')


def titulo(mensagem, numeroCor=0):
    tamanho = len(mensagem) + 4
    print(cores[numeroCor], end='')
    print('~' * tamanho)
    print(f' {mensagem} ')
    print('~' * tamanho)
    print(cores[0], end='')


comando = ''
while True:
    titulo('Sistema de ajuda PyHELP', 1)
    comando = str(input("Função ou Biblioteca: "))
    print(cores[0],end='')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Fim do programa',5)