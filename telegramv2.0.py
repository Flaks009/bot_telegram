import time
import config
from api_request import test_dol
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent


def handle(msg):
   content_type, chat_type, chat_id = telepot.glance(msg)
   print(content_type, chat_type, chat_type)

   if content_type == 'text':
      bot.sendMessage(chat_id, test_dol())

def on_inline_query(msg):
   def compute():
      query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
      print ('Inline Query:', query_id, from_id, query_string)

      articles = [InlineQueryResultArticle(
                     id='Test',
                     title='Inline Test',
                     input_message_content=InputTextMessageContent(
                           message_text='Inline Test'
                     )
                  )]

      return articles
   answerer.answer(msg, compute)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)

TOKEN = config.TOKEN
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat':handle,
                  'inline_query':on_inline_query,
                  'chosen_inline_result':on_chosen_inline_result
}).run_as_thread()
print('Listening...')

while True:
   time.sleep(10)