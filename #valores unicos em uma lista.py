#criar uma lista
valores = []
while True:
    numero = int(input('Digite um numero:'))
    if numero not in valores:
        valores.append(numero)
    else:
        print('Numero duplicado,Impossível adicionar.')

    pergunta = str(input('Deseja continuar[S/N]:')).upper[0]
    while pergunta not in 'SsNn':
        pergunta = str(input('Digite uma opção válida[S/N]:'))
