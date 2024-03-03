import math
#contar o total de numeros no for
total = 0
#ler um numero
num = int(input('Digite um numero:'))

for c in range(1,num+1):
    #definir quantos numeros no for são divisiveis
    if num % c == 0:
        #contabilizando o total de numeros divisiveis
        total += 1
        print('\033[31m', end=' ')

    else:
        print('\033[33m',end=' ')
    print(c, end=' ')


print('\nO numero {} foi dividido por {} numero(s).'.format(num, total))


if total > 2:
    print('O numero não é primo.')
elif total == 2:
    print('O numero é primo.')












