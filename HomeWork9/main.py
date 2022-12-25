
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN 
from bot_commands import *
from xo import game

updater = Updater(TOKEN)
dispetcher = updater.dispatcher

hello_handler = CommandHandler('hello', hello_command)
start_handler = CommandHandler('start', help_command)
help_handler = CommandHandler('help', help_command)
time_handler = CommandHandler('time', time_command)
sum_handler = CommandHandler('sum', sum_command)
diff_handler = CommandHandler('diff', diff_command)
prod_handler = CommandHandler('prod', prod_command)
div_handler = CommandHandler('div', div_command)
pow_handler = CommandHandler('pow', pow_command)
sqr_handler = CommandHandler('sqr', sqr_command)
game_handler = CommandHandler('xo', game)

message_handler = MessageHandler(Filters.text, get_message)


dispetcher.add_handler(hello_handler)
dispetcher.add_handler(time_handler)
dispetcher.add_handler(start_handler)
dispetcher.add_handler(help_handler)
dispetcher.add_handler(sum_handler)
dispetcher.add_handler(diff_handler)
dispetcher.add_handler(prod_handler)
dispetcher.add_handler(div_handler)
dispetcher.add_handler(pow_handler)
dispetcher.add_handler(sqr_handler)
dispetcher.add_handler(game_handler)
dispetcher.add_handler(message_handler)

print('сервер запущен')
updater.start_polling()
updater.idle()