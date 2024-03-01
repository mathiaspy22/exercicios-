soma = 0
cont = 0
#montar um range de 0 a 6
for c in range(1,7):
    # LER 6 NUMEROS INTEIROS
    num = int(input(f'Digite o {c}° numero:'))
    #somar os numeros pares apenas
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos pares dentre os {} numeros pares foi: {}'.format(cont,soma))







