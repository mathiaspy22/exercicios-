
#Ler um numero
numero = int(input('Digite um numero:'))
c = numero
f = 1
print('Calculando fatorial {}! = '.format(numero),end='')
while c > 0:
    print(c,end='')
    print('x' if c > 1 else '=',end='')
    f *=c
    c-=1
print('O fatorial de {}! é {}'.format(numero,f))





