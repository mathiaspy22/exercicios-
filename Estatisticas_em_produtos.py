print('*=*'*20)
print('====== ATACADÃO DOS MALUCO =======')
print('*=*'*20)
#declarando variáveis
produto_com_menor_preço = ''
menor = float('inf')
cont_above_mil = soma_produtos = 0
while True:
    #ler o nome
    nome_produto = str(input('Digite o nome do produto que você deseja:'))
    #ler o preço
    preço_produto = float(input('Digite o valor do produto:R$'))
    if preço_produto > 1000:
        cont_above_mil+=1
    #calculando o total dos preços
    soma_produtos+=preço_produto
    #definindo qual o menor preço da
    if preço_produto < menor:
        menor = preço_produto
        produto_com_menor_preço = nome_produto
    #adicionando a pergunta
    pergunta = str(input('Deseja adicionar mais algum produto [S/N]?')).strip().upper()[0]
    while pergunta not in 'SsNn':
        pergunta = str(input('Digite[S/N] para continuar:')).strip().upper()[0]
    if pergunta in 'Nn':
        break
print(f'O total de produtos acima de mil reais foram {cont_above_mil}.')
print(f'Sua compra foi concluida com sucesso, Você gastou um total de R${soma_produtos}.')
print(f'O menor valor que você pagou foi de R${menor}')
print(f'O produto que você mais economizou na compra foi em {produto_com_menor_preço.capitalize()}')
