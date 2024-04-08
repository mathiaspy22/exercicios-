palavras =('Grátis','Montanha','Luxo','Brigada',
            'Bloco','Lutarem','Jogarem',
           'Garou','Lula','Mãe','Pai','Pão')
letras = ''
vogais = 'aáãeéêiíîoóôuû'

for palavra in palavras:
    print(f'\nNa palavra {palavra} tem:',end=' ')
    for letras in palavra:
        if letras in vogais:
            print(letras,end=' ')
