#ler o primeiro termo
print('GERADOR DE PA')
print('*=*'*10)
#ler o primeiro termo
primeiro = int(input('Digite o primeiro termo:'))
#ler a razao
razao = int(input('Digite a razão da PA:'))

termo = primeiro
#contador dos termos
contador = 1
while contador <= 10:
    print('{}'.format(termo),end=' > ')
    contador += 1
    termo += razao
print('FIM')
