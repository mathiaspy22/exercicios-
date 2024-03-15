#ler o primeiro termo
primeiro_termo = int(input('Digite o primeiro termo:'))
#ler a razao
razao = int(input('Digite a razão da PA:'))
#contador de termos
contador = 1
termo = primeiro_termo
pergunta = 10
total = 0
#laço de repetição


while pergunta != 0:
    total+= pergunta

    while contador <= total:
        contador += 1
        primeiro_termo+=razao
        print(primeiro_termo,end=' > ')

    pergunta = int(input('Digite quantos termos mais:'))

print('Fim.\nO total de termos foi de {} termo(s) .'.format(contador-1))

