
numeros =(int(input('Digite um numero:')),
        int(input('Digite um numero:')),
        int(input('Digite um numero:')),
        int(input('Digite um numero:')))


if 3 not in numeros:
    print('O numero 3 não se encontra na lista.')

else:
    print(f'O numero 3 apareceu na {numeros.index(3) + 1}° posição.')

print(f'O numero 9 apareceu {numeros.count(9)}x')

for numero in numeros:
    if numero % 2 == 0:
        print(f'\nOs números pares são:{numero}',end=' ')






