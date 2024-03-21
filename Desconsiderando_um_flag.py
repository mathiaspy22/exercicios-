

#variavel para determinar a soma dos numeros
soma = 0
#variavel para contar quantos numeros foram digitados
contador = 0
while True:
    #lendo um numero inteiro
    num = int(input('Digite um numero[999 para parar]:'))

    if num == 999:
        break
    contador += 1
    soma+=num
print(f'A soma dos numeros digitados foram:{soma}')
print(f'A quantidade de numeros digitados foram {contador}')