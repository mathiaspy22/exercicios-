#lendo o a alternativa do usuario
import random
usuario = str(input('Digite, pedra, papel ou tesoura:')).strip().upper().lower()
#pondo as possbilidades da maquina
possbilidades = ['PEDRA'.upper().lower(),'PAPEL'.upper().lower(), 'TESOURA'.upper().lower()]
resposta_do_pc = random.choice(possbilidades)


#CONDIÇÃO PARA CASO DE EMPATE COM PEDRA


if usuario == 'PEDRA'.upper().lower() and resposta_do_pc == 'PEDRA'.lower():
    print('Sua resposta foi {} e a da maquina foi {}, vocês empataram.\nTente novamente!'.format(usuario,resposta_do_pc))
#CONDIÇÃO ONDE VC ESCOLHE SOMENTE PEDRA


elif usuario == 'PEDRA'.upper().lower() and resposta_do_pc == 'TESOURA'.lower():
    print('Você escolheu {} e a maquina {}, você ganhou!'.format(usuario,resposta_do_pc))

elif usuario == 'PEDRA'.upper().lower() and resposta_do_pc == 'PAPEL'.lower():
    print('Você escolheu {} e a maquina {}, você perdeu!\nTente novamente!'.format(usuario,resposta_do_pc))

# CONDIÇÃO PARA CASO DE EMPATE PAPEL


elif usuario == 'PAPEL'.upper().lower() and resposta_do_pc == 'PAPEL'.lower():
    print('Você escolheu {} e a maquina {} vocês empataram\nTente novamente!'.format(usuario,resposta_do_pc))

#CONDIÇÃO ONDE VC ESCOLHE SOMENTE PAPEL


elif usuario == 'PAPEL'.upper().lower() and resposta_do_pc == 'PEDRA'.lower():
    print('Você escolheu {} e a maquina {}, Você ganhou!'.format(usuario,resposta_do_pc))

elif usuario == 'PAPEL'.upper().lower() and resposta_do_pc == 'TESOURA'.lower():
    print('Você escolheu {} e a maquina {}, Você perdeu\nTente novamente!'.format(usuario,resposta_do_pc))

# CONDIÇÃO ONDE HÁ EMPATE DE TESOURA


elif usuario == 'TESOURA'.upper().lower() and resposta_do_pc == 'TESOURA'.lower():
    print('Você escolheu {} e a maquina {}, Vocês empataram\nTente novamente!'.format(usuario,resposta_do_pc))

#CONDIÇÃO ONDE VC SÓ ESCOLHE TESOURA


elif usuario == 'TESOURA'.upper().lower() and resposta_do_pc == 'PEDRA'.lower():
    print('Você escolheu {} e a maquina {}, Você perdeu!\nTente novamente!'.format(usuario,resposta_do_pc))

elif usuario == 'TESOURA'.upper().lower() and resposta_do_pc == 'PAPEL'.lower():
    print('Você escolheu {} e a maquina {}, Você ganhou!'.format(usuario,resposta_do_pc))
