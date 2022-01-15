#Crie uma função chamada voto() que recebe como parâmetro o ano de nascimento, retornando um valor literal indicado se uma
#pessoa tem voto 'NEGADO', 'OPCIONAL' ou 'OBRIGATÓRIO' nas eleições

def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    if idade >= 70 or (idade >= 16 and idade < 18):
        return (f'Com {idade} anos: VOTO OPCIONAL')
    elif idade < 16:
        return (f'Com {idade} anos: VOTO NEGADO')
    else:
        return (f'Com {idade} anos: VOTO OBRIGATÓRIO')


nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))