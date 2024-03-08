#perguntar o valor da casa

valor_casa = float(input('Digite o valor da casa desejada:R$'))

#perguntar o salário do comprador

salario_comprador = float(input('Digite o seu salário:'))

#perguntar em quantos anos ele deseja pagar

anos_a_pagar = int(input('Digite em quantos meses você vai querer pagar:'))

#descontando 30% do salario

desconto_salario = salario_comprador * 30/100

#diminuindo o desconto do salário

print('Os 30% do seu salário é R${:.2f}'.format(desconto_salario))

#calculando os meses a pagar por ano financiado

parcela_meses = anos_a_pagar * 12
print('Quantidade de meses: {} meses'.format(parcela_meses))

#valor das parcelas

valor_parcelas = valor_casa / parcela_meses
print('O valor das parcelas será R${:.2f}'.format(valor_parcelas))

if valor_parcelas > desconto_salario:
    print('Obrigado por usar nossos serviços.\nSeu financiamento infelizmente foi NEGADO! :-(')

elif valor_parcelas <= desconto_salario:
    print('Obrigado por usar nossos serviços.\nSeu financiamento foi ACEITO! :-)')