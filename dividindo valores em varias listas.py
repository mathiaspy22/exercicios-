lista1 = []
lista2 = []
lista3 = []
#ler varios numeros
while True:
    numeros = int(input('Digite um valor:'))
    lista1.append(numeros)
    if numeros % 2 == 0:
        lista2.append(numeros)

    if numeros % 2 == 1:
        lista3.append(numeros)

    pergunta = str(input('Deseja continuar[S/N]?')).strip().upper()[0]
    while pergunta not in 'SsNn':
        pergunta = str(input('Digite uma resposta válida[S/N]:'))
    if pergunta in 'Nn':
        break



print(f'A lista completa é {lista1}.')
print('Os numeros pares da lista são:')
print(lista2)
print('Os numeros impares da lista são:')
print(lista3)