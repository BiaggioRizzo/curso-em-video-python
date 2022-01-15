#Lei idade e sexo de várias pessoas e mostre quantas pessoas tem mais de 18 anos,
# quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos

maiorIdade = homemCadastrado = mulherMenorIdade = 0

while True:
    idade = int(input("Digite sua idade: "))
    #Foi utilizado while sexo not in 'MF', pois é uma forma de segurança para
    #usuário não digitar uma Palavra diferente de M ou F
    sexo = resposta = ' '  #importante se deixa string sem espaço não funciona
    while sexo not in 'MF':
        sexo = str(input("Digite seu sexo M/F: ")).strip().upper()[0]
    
    if idade >= 18:
        maiorIdade += 1
    if sexo == 'M':
        homemCadastrado += 1
    if sexo == 'F' and idade < 18:
        mulherMenorIdade += 1
             
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar S/N?  ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'''
Foram no total {homemCadastrado} homens cadastrados.
Total de pessoas maiores de idade foram {maiorIdade}.
Tiveram {mulherMenorIdade} mulheres menores de idade.
''')