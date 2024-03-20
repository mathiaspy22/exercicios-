#atribuir zero a variavel numero para que o while não dê erro

#respostas
resposta_positiva = 's'.upper()[0]
resposta_negativa = 'n'.upper()[0]
cont = 1
soma = 0
maior = 0
menor = 0
pergunta = str(input('Deseja continuar[S/N]:'))
#condição de repetição para as perguntas abaixo
while pergunta in 'Ss':
    numeros = int(input('Digite um numero:'))
    pergunta = str(input('Deseja conitnuar[S/N]:')).strip().upper()[0]
    #definindo qual é o maior numero
    if numeros > maior:
        maior = numeros


    #contando quantos numeros foram usados
    cont+=1
    #somando os numeros do while
    soma+=numeros
#calculando a média
média = soma/(cont-1)



print('O maior numero dentre os {} digitados é {}'.format(cont-1,maior))
print('A media dos numeros será {}'.format(média))
print('A quantidade de numeros usados foi {} numero(s).'.format(cont-1))
print('A soma total dos numeros digitados foram {}'.format(soma))





