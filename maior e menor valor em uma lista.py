#ler 5 valores numericos e guarda-los em uma lista
import random
maior_valor = menor_valor = 0
valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite o valor para a posição {c}: ')))
    if c == 0:
        maior_valor = menor_valor = valores[c]
    else:
        if valores[c] > maior_valor:
            maior_valor = valores[c]
        if valores[c] < menor_valor:
            menor_valor = valores[c]

print(f'O maior valor é {maior_valor} nas posições',end=' ')

for indice, valor in enumerate(valores):
    if valor == maior_valor:
        print(f'{indice}...',end='')

print(f'\nO menor valor é {menor_valor} nas posições',end=' ')

for indice , valor in enumerate(valores):
    if valor == menor_valor:
        print(f'{indice}...',end='')


