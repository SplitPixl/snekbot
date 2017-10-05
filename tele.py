#import telegram
from telegram.ext import Updater, CommandHandler
import random

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def hss(bot, update):
    update.message.reply_text(update.message.text.replace('/hss', ''))

def pls(bot, update):
    update.message.reply_text(':snake:')

def whomade(bot, update):
    update.message.reply_text('splitpixl made snekbot')

def info(bot, update):
    update.message.reply_text('snekbot was coded in python with the library python-telegram-bot. hss.')

def invite(bot, update):
    update.message.reply_text('to use snekbot in your groups click this: https://snek.splitpixl.xyz/')

def intensifies(bot, update):
    update.message.reply_text('https://snek.splitpixl.xyz/intense.gif')

def hello(bot, update):
    update.message.reply_text('hello yes this is snek.')

def noboop(bot, update):
    update.message.reply_text('https://snek.splitpixl.xyz/noboop.jpg')

def sourcecode(bot, update):
    update.message.reply_text('https://github.com/SplitPixl/snekbot')

def snek(bot, update):
    sneks = ['snek', 'hss', 'ssssnek', 'slither', 'snek sneek']
    update.message.reply_text(random.choice(sneks))

updater = Updater(open('./token.telegram','r').read().replace('\n', ''))

updater.dispatcher.add_handler(CommandHandler('hss', hss))
updater.dispatcher.add_handler(CommandHandler('pls', pls))
updater.dispatcher.add_handler(CommandHandler('whomade', whomade))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('invite', invite))
updater.dispatcher.add_handler(CommandHandler('intensifies', intensifies))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('noboop', noboop))
updater.dispatcher.add_handler(CommandHandler('sourcecode', sourcecode))
updater.dispatcher.add_handler(CommandHandler('snek', snek))

updater.start_polling()
updater.idle()
