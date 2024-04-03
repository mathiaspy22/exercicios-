valor = 1
valor1 = int(input('Digite um numero:'))
valor2 = int(input('Digite outro numero:'))
valor3 = int(input('Digite mais um numero:'))
valor4 = int(input('Digite um ultimo numero:'))
tupla_valores = (valor ,valor1,valor2,valor3,valor4)
print(f'O numero 9 apareceu {tupla_valores.count(9)}x.')


if 3 in tupla_valores:
    print(f'O numero 3 apareceu a primeira vez na posição {tupla_valores.index(3)}')

if 3 not in tupla_valores[0:]:
    print('O numero 3 não está na tupla.')


print('Os numeros da lista superior que são pares:')
for numeros in tupla_valores:
    if numeros % 2 == 0:
        print(numeros,end=' ')
