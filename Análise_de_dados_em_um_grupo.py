sexo = ' '
contador_de_usuarios = 0
cont_idade = 0
cont_sexo_masculino = 0
cont_sexo_feminino = 0
while True:
    contador_de_usuarios += 1
    print(f'----====---====---- CADASTRE A {contador_de_usuarios}º PESSOA ----====---====----')
    #ler o sexo
    sexo = str(input('Sexo[M/F]:')).strip().upper()[0]
    #caso o usuário digite um sexo inválido
    while sexo not in 'MmFf':
        sexo = str(input('Digite seu sexo corretamente! ->[M/F]<-:')).strip().upper()[0]
    #condição para contabilizar quantos homens foram cadastrados
    if sexo in 'Mm':
        cont_sexo_masculino+=1
    #ler a idade
    idade = int(input('Digite sua idade:'))
    # condição para contabilizar quantas mulheres tem menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        cont_sexo_feminino+=1
    #condição para contabilizar quantas pessoas tem mais de 18 anos
    if idade > 18:
        cont_idade+=1
    #caso o usuário digite uma idade invalida
    while idade <= 0:
        idade = int(input('Digite uma idade válida:'))
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = str(input('Deseja continuar [S/N]?')).strip().upper()[0]

    if pergunta in 'Nn':
        break
print(f'A quantidade mulheres abaixo de 20 anos cadastradas foram de {cont_sexo_feminino} indivídua(s).')
print(f'A quantidade de homens cadastrados foram de {cont_sexo_masculino} indíviduo(s).')
print(f'A quantidade de pessoas maiores de 18 anos são de {cont_idade} pessoa(s).')



