from random import randint
#ler a velocidade do carro
velocidade = randint(1,150)
print('A velocidade flagrada pelo carro foi de {}Km/h'.format(velocidade))
#condição caso ele passe os 80km
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80km/h\nSua multa será de R${:.2f}'.format((velocidade - 80) * 7.00))
else:
    print('Tenha um bom dia! Dirija com segurança.')