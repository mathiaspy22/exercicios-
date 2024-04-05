tuplas_de_palavras = ('Lutar','Programar','Jogar','Gozar','Mudar')
vogais = 'aeiou'
letras = ' '
for palavras in tuplas_de_palavras:
    print(f'\nNessa palavra {palavras} temos as vogais:',end=' ')
    for letras in palavras:
        if letras in vogais:
            print(letras,end=',')