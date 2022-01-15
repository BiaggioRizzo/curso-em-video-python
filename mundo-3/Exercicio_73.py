#Preencha na tupla os 20 times do campeonato brasileiro.
# Apresente os 5 primeiros, os últimos 4 da tabela, coloque em ordem alfabetica
#Posição da tabela do time Chapecoense


tabela = ("Atlético-MG","Palmeiras","Flamengo","Fortaleza","Bragantino","Corinthians",
"Fluminense","Cuiabá","Internacional","Atletico-GO","Athelico-PR","Ceará","Santos",
"Juventude","Bahia","São Paulo","América-MG","Grêmio","Sport","Chapecoense")

print(f"Os cinco primeiros times são:{tabela[0:5]}")
print(f"Os quatro últimos times são: {tabela[-4:]}")
print(sorted(tabela))
print(f"O time da Chapecoense esta na posição {(tabela.index('Chapecoense')+1)} na tabela.")
 