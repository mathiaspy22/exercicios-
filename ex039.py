import datetime

ano_atual = datetime.date.today().year
#ler o ano do nascimento
ano_de_nascimento = int(input('Digite o ano do seu nascimento:'))
#calcular idade
idade = ano_atual - ano_de_nascimento
#ano em que a pessoa ira fazer 18 anos
ano_do_serviço = ano_de_nascimento + 18


#CONDIÇÃO PARA CASO A PESSOA TENHA MAIS DE 18 ANOS
if idade > 18:
    print('Você já tem {} anos'.format(idade))
    pergunta = str(input('Você já se alistou?')).strip()
    if pergunta == 'SIM'.upper().strip().lower():
        print('Ah! que bom. Se estiver ocorrido tudo certo, seu alistamento foi em {}.'.format(ano_do_serviço))
    elif pergunta == 'NÃO'.upper().strip().lower() or 'NAO'.upper().strip().lower():
        print('Você está em débito com o serviço militar, seu alistamento ocorreu em {}.'.format(ano_do_serviço))


#CONDIÇÃO PARA CASO A PESSOA TENHA 18 ANOS EXATOS
elif idade == 18:
    print('Você já tem {} anos.'.format(idade))
    pergunta = str(input('Você já se alistou?')).strip()
    if pergunta == 'SIM'.upper().lower().strip():
        print('Você deve ir na junta na data demarcada.')
    elif pergunta == 'NAO'.upper().strip().lower() or 'NÃO'.upper().strip().lower():
        print('Você deve marcar a data pra comparecer na junta o quanto antes possível.')


#CONDIÇÃO PARA CASO A PESSOA TENHA MENOS DE 18 ANOS
elif idade < 18:
    print('Você tem {} anos.'.format(idade))
    pergunta = str(input('Você já se alistou?')).strip()
    if pergunta == 'NÃO'.upper().lower().strip() or 'NAO'.upper().strip().lower():
        print('Você ainda não está com idade para se alistar, seu processo de alistamento será em {}'.format(ano_do_serviço))
    elif pergunta == 'SIM'.upper().lower().strip():
        print('?')

while ano_de_nascimento == 2003:
    continue