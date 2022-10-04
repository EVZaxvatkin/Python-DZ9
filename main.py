from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token=' ')
updater = Updater(token=' ')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет!\nМеня зовут Знайка.\nЯ учусь распознавать ваши тексты.\nЕсли я увижу в слове сочетание букв "абв", я очищу текст от этих слов.\nПроверь меня?')

def pravilo(update, context):
    text = update.message.text
    try:
        find_txt = "абв"
        lst = [i for i in text.split() if find_txt not in i]
        result = " ".join(lst)
        context.bot.send_message(update.effective_chat.id, f'Вот так: {result}')
    except:
        context.bot.send_message(update.effective_chat.id, 'Я не нашел ошибок')



start_handler = CommandHandler('start', start)
pravilo_handler = MessageHandler(Filters.text, pravilo)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(pravilo_handler)

updater.start_polling()
updater.idle()
