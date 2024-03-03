#Digitar uma frase
frase = (input('Digite uma frase:')).strip().upper()
#separar as palavras em uma lista
palavras = frase.split()

junto = ''.join(palavras)
#proximo passo é varrer a string de trás pra frente
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
    #printar a string invertida e normal
print(junto,inverso)
#definir se a string é um palíndromo ou não
if junto == inverso:
    print('Temos um palindromo.')

else:
    print('{} não é um palíndromo.'.format(junto))