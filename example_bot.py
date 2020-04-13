import time
import telepot

# Comandos que vem do software Telegram e sao processados pela Raspberry PI
def handle(msg):
   chat_id = msg['chat']['id']  # recebe a mensagem do  Telegram
   comando = msg['text']  # recupera o texto da mensagem
   print ('comando recebido: %s' % comando)
 
   if comando == 'Ola':
      bot.sendMessage (chat_id, str("Test message."))
 
# Permite que os comandos digitados no telegram sejam enviados a Raspberry PI
bot = telepot.Bot('bot id')
bot.getMe()
bot.message_loop(handle)
print('Hold on...')
 
while True:
   time.sleep(10)

