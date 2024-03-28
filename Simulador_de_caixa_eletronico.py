#ler um valor inteiro
valor = int(input('Digite um numero:'))
total = valor
cédulas = 100
total_de_cédulas = 0


while True:
    if total >= cédulas:
        total-=cédulas
        total_de_cédulas += 1

    else:
        if total_de_cédulas > 0:
            print(f'O valor inserido irá te retornar {total_de_cédulas} cédulas de R${cédulas}.')
        if cédulas == 100:
            cédulas = 50
        elif cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 5
        elif cédulas == 5:
            cédulas = 2

