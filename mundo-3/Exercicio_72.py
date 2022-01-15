#Preencha uma tupla com números extenso, de zero até vinte e mande usuário 
#digitar número entre 0 a 20 e mostrar por extenso.

extenso = ("Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")
numero = int(input("Digite um número: "))    
while True:
    if numero >= 0  and numero <= 20 :  ## if 0<= numero <= 20
        break
    else:
        numero = int(input("Digite novamente um número entre 0 e 20: "))

print(f"Você digitou {extenso[numero]}")