from telegram.ext import CallbackContext
from telegram import Update
import time, math
from logger import write_log
import logger as log

def get_message(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if 'прив' in message: 
        update.message.reply_text(f'Привет') 
        return None 
    update.message.reply_text(f'вы ввели: {message},\n я не понял, что вы хотите сделать\nнажмите /help, чтобы узнать, что я умею.')  


def hello_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    update.message.reply_text(f'Привет, {update.effective_user.first_name}!\nЧто будем делать? \nнажмите /help, чтобы узнать, что я умею.')


def help_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    update.message.reply_text(f'/hello\n/time\n/help\n/sum\n/diff\n/prod\n/div\n/pow\n/sqr\n/game')


def time_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    update.message.reply_text(f'{time.ctime(time.time())}')  #{datetime.datetime.now().time()}



def sum_command(update: Update, context: CallbackContext):
    write_log(update, context)
    update.message.reply_text(f'введите команду /sum первое число пробел второе число')
    msg = update.message.text
    print(msg)
    items = msg.split() # тут мы получим: /sum первое_число второе_число (в списке)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

def diff_command(update: Update, context: CallbackContext):
    write_log(update, context)
    update.message.reply_text(f'введите команду /diff первое число пробел второе число')
    msg = update.message.text
    print(msg)
    items = msg.split() # тут мы получим: /diff первое_число второе_число (в списке)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')


def prod_command(update: Update, context: CallbackContext):
    write_log(update, context)
    update.message.reply_text(f'введите команду /prod первое число пробел второе число')
    msg = update.message.text
    print(msg)
    items = msg.split() # тут мы получим: /prod первое_число второе_число (в списке)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x*y}')


def div_command(update: Update, context: CallbackContext):
    write_log(update, context)
    update.message.reply_text(f'введите команду /div первое число пробел второе число')
    msg = update.message.text
    print(msg)
    items = msg.split() # тут мы получим: /div первое_число второе_число (в списке)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} / {y} = {x/y}')
            

def pow_command(update: Update, context: CallbackContext):
    write_log(update, context)
    update.message.reply_text(f'введите команду /diff первое число пробел второе число')
    msg = update.message.text
    print(msg)
    items = msg.split() # тут мы получим: /pow первое_число второе_число (в списке)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} ** {y} = {x**y}')
     

def sqr_command(update: Update, context: CallbackContext):
    write_log(update, context)
    update.message.reply_text(f'введите команду /sqr первое число пробел второе число')
    msg = update.message.text
    print(msg)
    items = msg.split() # тут мы получим: /diff первое_число второе_число (в списке)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'корень из {x} = {round(math.sqrt(x), 5)}')
    
     
