import random
from random import shuffle
soma = 0
maior = 0
menor = 0
nome_do_mais_velho = ''
contador_de_mulheres = 0
#Lendo o nome
for pessoas in range (1,5):
    print('====---==== {}° PESSOA ====---===='.format(pessoas))
    nome = str(input('Digite o nome:').strip())
    idade = int(input('Digite sua idade: '))
    #SOMANDO as idades
    soma += idade
#LENDO O SEXO DOS INDIVIDUOS
    sexo = str(input('Sexo[F/M]:')).strip()
# definindo qual é a maior idade e o nome do mais velho
    if pessoas == 1 and sexo in 'Mm':
        maior = idade
        nome_do_mais_velho = nome
    if sexo in 'Mm'and idade > maior:
        maior = idade
        nome_do_mais_velho = nome
#definir quantas mulheres tem 20 anos
    if sexo in 'Ff' and idade < 20:
        contador_de_mulheres += 1
#definindo a média de idade das pessoas
media_idade = soma/pessoas
#PRINTANDO RESULTADO FINAL
print(('A média de idade do grupo de {} anos.'.format(int(media_idade))))
print('O homem com mais idade tem {} anos e se chama {} '.format(maior,nome_do_mais_velho))
print('Existem um total de {} mulhere(s) abaixo dos 20 anos'.format(contador_de_mulheres))







