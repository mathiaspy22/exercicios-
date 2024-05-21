lista1 = []
lista2 = []
lista3 = []
while True:
    numeros = int(input('Digite um numero:'))

    pergunta = str(input('Deseja continuar?')).strip().upper()[0]
    lista1.append(numeros)

    if numeros % 2 == 0:
        lista2.append(numeros)

    elif numeros % 2 == 1:
        lista3.append(numeros)

    if pergunta in 'Nn':
        break
print(f'Os numeros totais digitados foram: {lista1}.')
print(f'Os números pares da lista são: {lista2}.')
print(f'Os números impares da lista são:{lista3}.')