import time
import sys
import telepot
from telepot.loop import MessageLoop

# Permite que os comandos digitados no telegram sejam enviados a Raspberry PI
#bot = telepot.Bot('961146795:AAGH2RzfahI1qtqJqtSYyUf6Y0gQQ8jenl4')
#bot.getMe()

def handle(msg):
   content_type, chat_type, chat_id = telepot.glance(msg)
   print(content_type, chat_type, chat_type)

   if content_type == 'text':
      bot.sendMessage(chat_id, 'Sonic Judeu') 

TOKEN = sys.argv[1]
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening...')

while True:
   time.sleep(10)