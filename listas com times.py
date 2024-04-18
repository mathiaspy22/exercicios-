lista_brasileirao = ('','Bahia','Criciuma','Atlético Mineiro','Atlético Goianiense',
                     'Flamengo','Ribeirão Preto','Fluminense','Botafogo','Cruzeiro',
                     'Cuiabá','Fortaleza','Grêmio','Internacional','Palmeiras','Juventude'
                     ,'Bragantino','Chapecoense','São Paulo','Vitória','Corinthias')
print('-=-'*20)
print(f'-A posição dos 5 primeiros times é: {lista_brasileirao[1:6]}')
print('-=-'*20)
print(f'-Os 4 ultimos colocados são: {lista_brasileirao[16:20]}')
print('-=-'*20)
print(f'-Os times ordenados em ordem alfabética é: {sorted(lista_brasileirao[1:])}')
print('-=-'*20)
print(f'A chapecoense está na posição: {lista_brasileirao.index("Chapecoense")}°')