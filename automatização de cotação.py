import time
import pyautogui
import pyperclip
import yfinance
import mouseinfo
import random
ticker = input('Digite o código da ação:')
dados =(yfinance.Ticker('PBR-A').history('8mo'))
fechamento = dados.Close
fechamento_maximo = fechamento.max()
fechamento_minimo = fechamento.min()
cotacao_atual = round(fechamento[-1],2)
cotacao_minima = round(fechamento_minimo,2)
cotacao_maxima = round(fechamento_maximo,2)
ultima_cotacao_catalogada = cotacao_atual
mensagem = (f'Segue os dados das Análises da {ticker}:\n Cotação atual:R${(cotacao_atual)}\n Cotação máxima:R${cotacao_maxima}\n Cotação minima:R${cotacao_minima}\n Segue com atenção os dados das análises\n Att. Mathias.')
#enviar um email para o gestor com os resultados das analises
posicao_mouse = pyautogui.position()
time.sleep(7)
print(posicao_mouse)
pyautogui.PAUSE = 2
#sair do pycharm
pyautogui.click(676,751)
#abrir uma nova aba
pyautogui.hotkey('ctrl','t')
#entrar no gmail
pyperclip.copy('www.gmail.com')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('Enter')
#clicar no botao escrever
pyautogui.click(95,183)
#clicar no destinatario e escrever o email do proprio
pyautogui.click(847,307)
pyperclip.copy('contato.matheusbnogueira@gmail.com')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('Enter')
#escrever o assunto do email
pyautogui.click(802,375)
pyperclip.copy('Análise de finanças')
pyautogui.hotkey('Ctrl','v')
pyautogui.hotkey('Enter')
#escrever o relatório em si no corpo do email
pyautogui.click(802,389)
pyperclip.copy(mensagem)
pyautogui.hotkey('Ctrl','v')
pyautogui.hotkey('Enter')
#enviar o email(apertar enter)
pyautogui.click(832,694)















