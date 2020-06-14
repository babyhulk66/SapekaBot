from random import choice, randint
from datetime import timedelta
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

viados = ['Anderson', 'Wesley', 'Fernanda', 'Lucimara', 'Pablo']
viado_do_dia = choice(viados)

def help(update, context):
        update.message.reply_text('Não vou ajudar em nada deixa de ser burro')

def viado_daily(context: CallbackContext):
        """seleciona o viado do dia"""
        global viado_do_dia
        viado_do_dia = choice(viados)
        context.bot.send_message(chat_id=context.job.context, text="{} é o viado do dia 👏🏿👏🏿👏🏿".format(viado_do_dia))

def repeat_viado_daily(update: Update, context: CallbackContext):
        """faz o viado ser escolhido todos os dias na hora que foi dado /start"""
        context.job_queue.run_repeating(viado_daily, timedelta(days=1), 0, context=update.message.chat_id)

def viado(update, context):
        """mostra o viado do dia"""
        update.message.reply_text("viado do dia é {}!!!".format(viado_do_dia))

def queimadoido(update, context):
        """POW"""
        context.bot.send_message(chat_id=update.message.chat_id, text='pra pra pra pra pra pra')
        context.bot.send_message(chat_id=update.message.chat_id, text='pra')
        context.bot.send_message(chat_id=update.message.chat_id, text='pra pra pra pra pra')
        context.bot.send_message(chat_id=update.message.chat_id, text='POOOOOWW')

def bolsomitometro(update, context):
        """seleciona um número de 0 a 100 pra ser sua porcentagem de bolsominion"""
        update.message.reply_text("você é {}% bolsominion 😎👉👉".format(randint(0, 100)))

def viadometro(update, context):
        """seleciona um número de 0 a 100 pra ser a porcentagem de viadão de quem foi botado no argumento do comando"""
        update.message.reply_text("{} é {}% viadão 🌈🍆".format(" ".join(context.args), randint(0, 100)))

def sapatometro(update, context):
        """seleciona um número de 0 a 100 pra ser a porcentagem de sapatão de quem foi botado no argumento do comando"""
        update.message.reply_text("{} é {}% sapatão 🌈🍑".format(" ".join(context.args), randint(0, 100)))

def main():
        updater = Updater("token é segredo meia noite eu conto", use_context=True)

        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", repeat_viado_daily))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("viado", viado))
        dp.add_handler(CommandHandler("queima", queimadoido))
        dp.add_handler(CommandHandler("bolsominion", bolsomitometro))
        dp.add_handler(CommandHandler("viadometro", viadometro))
        dp.add_handler(CommandHandler("sapatometro", sapatometro))

        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
        main()
