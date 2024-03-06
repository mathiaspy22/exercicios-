import datetime
from random import randint as numeroaleatorio
#definir o ano
ano = datetime.date.today().year

#definir quem tem ou não tem dezoito
cont1 = 0
cont2 = 0

#fazer um range
for c in range(1,8):
    ano_de_nascimento = int(input('Em que ano a {}° nasceu:'.format(c)))
    idade = ano - ano_de_nascimento
    print('O {}° individuo tem {} anos'.format(c,idade))

# contar quantos são maiores de idade
    if idade >= 21:
        cont1 += 1

#contar quantos são menores de idade
    if idade < 21:
        cont2 += 1
print('Só há apenas {} pessoa(s) maiores de idade\nE {} pessoa(s) menores de idade'.format(cont1,cont2))






