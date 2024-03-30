pergunta = ' '
numero_em_extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    #ler um numero
    numero = int(input('Digite um numero de 0 a 20:'))


    if numero in range(0,21):
        print(f'Você escreveu o numero: {numero_em_extenso[numero]}.')
        pergunta = str(input('Deseja continuar[S/N]?')).strip().upper()[0]
        while pergunta not in 'SsNn':
            pergunta = str(input('Opção inválida,Deseja continuar[S/N]:')).strip().upper()[0]
        if pergunta == 'N':
            break

    else:
        retorno = int(input('Alternativa inválida, digite um numero de 0 a 20:'))
        print(f'Você escreveu o numero: {numero_em_extenso[retorno]}.')
        pergunta = str(input('Deseja continuar[S/N]?')).strip().upper()[0]
        while pergunta not in 'SsNn':
            pergunta = str(input('Opção inválida, Deseja continuar[S/N]:')).strip().upper()[0]
        if pergunta == 'N':
            break
print('Fim do programa.')