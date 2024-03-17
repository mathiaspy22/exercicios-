#ler um n
termos = int(input('Digite quantos termos você quer mostrar?'))
#devido a ja termos lido o primeiro e segundo termo, o contador começa em 3

#ler os primeiros termos
t1 = 0
t2 = 1
#devido a ja termos lido o primeiro e segundo termo, o contador começa em 2
cont = 2
print('{} >'.format(t1,t2),end=' ')
while cont <= termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print('{} >'.format(t3),end=' ')

print('FIM')

