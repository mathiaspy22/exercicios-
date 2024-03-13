#ler dois valores
valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
opções = 0

while opções != 5:
    opções = int(input('Qual opção você deseja:'))
    print('\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR NUMERO\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA')
    print('=*='*20)
    #IMPOR A CONDIÇÃO PARA SOMAR OS NUMEROS
    if opções == 1:
        soma = valor1 + valor2
        print('A soma entre {} + {} é igual a {}'.format(valor1,valor2,soma))
        print('=*=' * 20)
    #IMPOR A CONDIÇÃO PARA MULTIPLICAR OS NUMEROS
    elif opções == 2:
        multiplicação = valor1 * valor2
        print('A multiplicação {} x {} é igual a {}'.format(valor1,valor2,multiplicação))
        print('=*=' * 20)
    #IMPOR A CONDIÇÃO PARA SABER QUAL É O MAIOR E PARA CASO AMBOS SEJAM IGUAIS
    elif opções == 3:
        if valor1 > valor2:
            maior = valor1
            print('O maior valor dentre os dois {}'.format(maior))
            print('=*=' * 20)
        else:
            if valor2 > valor1:
                maior = valor2
                print('O maior valor dentre os dois numeros é {}'.format(maior))
                print('=*='*20)
            else:
                if valor1 == valor2:
                    print('Não há valor, ambos são iguais.')
                    print('=*='*20)
    elif opções == 4:
        valor1 = int(input('Digite um novo primeiro valor:'))
        valor2 = int(input('Digite um novo segundo valor:'))

    elif opções == 5:
        print('SAINDO DO SISTEMA...')