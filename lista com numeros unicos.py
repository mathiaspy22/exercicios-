#criar uma lista
lista = []
#ler inumeros números
while True:
    valores = int(input('Digite um valor:'))
    if valores not in lista:
        lista.append(valores)
    else:
        print('Numero duplicado, impossível adicionar.')
    pergunta = str(input('Deseja continuar[S/N]:')).strip().upper()[0]
    while pergunta not in 'SsNn':
        pergunta = str(input('Digite uma opção válida[S/N]:'))
    if pergunta in 'Nn':
        break

print(sorted(lista))