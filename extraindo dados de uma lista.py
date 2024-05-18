#criar uma lista
lista = []
contnumeros = 0
#ler varios numeros
while True:
    n = int(input('Digite um numero:'))
    #adiciona-los a lista
    lista.append(n)
    #quantos numeros foram digitados
    contnumeros+=1
    #perguntar se deseja parar
    pergunta = str(input('Deseja continuar?')).upper()[0].strip()[0]

    if pergunta in 'Nn':
        break

if 5 not in lista:
    print('Não há o numero 5 na lista.')
else:
    print('Há o numero 5 na lista')

print(f'A quantidade de numeros digitados foi {contnumeros} numero(s).')

lista.sort(reverse=True)
print(f'A lista em formato descrescente é: {lista}.')