#Crie uma função chamada notas() que pode receber várias notas e retorna um dicionário as seguintes informações
# Quantidade de notas | A maior nota | A menor nota | A média da turma | A situação (opcional)

def notas(* notas, situacao=False):
    """-> Funcao para analisar notas e situacao de alunos.
    :param notas: Um ou mais notas dos alunos.
    :param situacao: (Opcional) Indica se deve ou nao mostra a situacao do aluno. Lista das seguintes situacoes:
    Media acima 8.5 = Excelente
    Media entre 6 e 8.4 = Boa
    Media entre 4 e 5.9 = Razoavel
    Media abaixo 4 = Ruim
    """
    ficha = dict()  #[]
    maiorNota = menorNota = media = somaNota =  0
    for valor in notas:
        if valor >= maiorNota or maiorNota == 0:
            maiorNota = valor
        if valor <= menorNota or menorNota == 0:
            menorNota = valor
        somaNota += valor       #Podia substituir somaNota pela variável média, decide manter somaNota para deixar coerente
    
    ficha['totalNotas'] = len(notas)
    media = somaNota / ficha['totalNotas']
    ficha['media'] = media
    ficha['maior'] = maiorNota
    ficha['menor'] = menorNota
    if situacao == True:
        if ficha['media'] >= 8.5:
            ficha['situação'] = 'Excelente'
        elif ficha['media'] >= 6 and ficha['media'] < 8.5:
            ficha['situação'] = 'Boa'
        elif ficha['media'] >= 4 and ficha['media'] < 6:
            ficha['situação'] = 'Razoável'
        else:
            ficha['situação'] = 'Ruim'
    return ficha


print(notas(8,9, situacao=True))
help(notas)