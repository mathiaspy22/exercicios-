import time
from random import randint
#fazer o pc pensar um numero
usuario = int(input('Pense em um numero:'))
print(20*'=')
print('PROCESSANDO...')
time.sleep(1)
numero = (randint(0,5))
if numero == usuario:
    print('Você acertou! O numero pensado pelo PC foi {} e o numero escolhido por você foi {}. Parábens!'.format(numero,usuario))
else:
    print('Você errou :-(, o numero escolhido pelo PC foi {} e o seu {}, tente denovo! :-)'.format(numero,usuario))
