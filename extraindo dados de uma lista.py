cont = 0
#criar uma lista
lista = []
#ler varios numeros
while True:
    valores = int(input('Digite um numero:'))
    lista.append(valores)
    cont+=1
    pergunta = str(input('Deseja continuar[S/N]?')).strip().upper()[0]
    while pergunta not in 'SsNn':
        pergunta = str(input('Digite uma opção válida[S/N]:')).strip().upper()[0]
    if pergunta in 'Nn':
        break

print(f'A quantidade de números digitados foi {cont}')
print(f'A lista final de valores foi {lista}')
lista.sort(reverse=True)
print(f'A lista de maneira descrente fica {lista}')



