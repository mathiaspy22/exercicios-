import random
from random import randint as numero_aleatorio
maior = float('-inf')
#gerar 5 numeros aleatorios

#criar uma tupla
lista_numeros = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
print(f'Os valores sorteados foram:{lista_numeros}')
#DEFININDO QUAL É O MAIOR
print(f'O maior numero da lista foi {max(lista_numeros)}')
print(f'O menor numero da lista foi {min(lista_numeros)}')