
while True:
    pergunta = int(input('Digite qual numero você deseja mostrar a tabuada:'))

    if pergunta < 0:
        print('PROGRAMA DE TABUADA ENCERRADO, Valor inválido pra uma tabuada.')
        break

    print(f'Tabuada de {pergunta} mostrada.')
    print('=-='*4)


    for c in range(1,11):
        print(f'{pergunta} x {c} = {pergunta*c}')


