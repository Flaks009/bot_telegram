import time
import telepot

# Comandos que vem do software Telegram e sao processados pela Raspberry PI
def handle(msg):
   chat_id = msg['chat']['id']  # recebe a mensagem do  Telegram
   comando = msg['text']  # recupera o texto da mensagem
   print ('comando recebido: %s' % comando)
 
   if comando == 'Ola':
      bot.sendMessage (chat_id, str("Oi, incompetente do caralho. DO CARALHO."))
 
# Permite que os comandos digitados no telegram sejam enviados a Raspberry PI
bot = telepot.Bot('961146795:AAGH2RzfahI1qtqJqtSYyUf6Y0gQQ8jenl4')
bot.getMe()
bot.message_loop(handle)
print('Esperando Comando...')
 
while True:
   time.sleep(10)

