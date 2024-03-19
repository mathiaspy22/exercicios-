#ler varios numeros inteiros pelo teclado

soma = 0
contador = 1
numero = 0

while numero != 999:
    numero = int(input('Digite um numero[999 para parar]:'))
    soma+=numero
    contador+=1

print('Condição de parada atingida!\nA soma de todos os numeros serã {}\nOs numeros contados foram {} numero(s).'.format(soma-999,contador-1))





