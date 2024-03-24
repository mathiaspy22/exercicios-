import random
from random import randint
cont = 0
while True:
    tipo = ' '
    #ler a resposta do usuário
    usuario = int(input('Digite um numero:'))
    #ler as possibilidades do computador
    pc = random.randint(0,10)

    while tipo not in 'PI':
        tipo = str(input('Par ou impar[P/I]:')).upper().strip()[0]
    soma = pc + usuario

    if tipo == 'P' and soma % 2 == 0 or tipo == 'I' and soma % 2 != 0:
            print(f'Você colocou {usuario} e o Computador colocou {pc}\nO total deu {soma}\nYou WIN!')
            print('-=-'*10)
            print('Tente novamente...')
            print('-=-'*10)
            cont += 1


    if tipo == 'I' and soma % 2 == 0 or tipo == 'P' and soma % 2 != 0:
        break




print(f'Você perdeu. Porém venceu num total de {cont}x.')
