#Leiia um numero inteiro e mostre os primeiros elementos de uma sequência de Fibonacci

t1 = 0
t2 = 1
print('~'*26)
n = int(input('Quantos termos deseja? '))
print('~'*26)
count = 3
print('{} -> {} '.format(t1,t2),end='')

while count <= n:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1