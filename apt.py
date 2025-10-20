mport telebot
from telebot import types
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
bot = telebot.TeleBot('8179759241:AAGrBMXOPBOrqRPpPHp1U69UgsXbvzNDKYM')
# Создаем объект чатбота
bot = ChatBot('MyBot')

@bot.message_handler(commands=['start'])
def get_text_messages(message):
   
   if (message.text == "/start"):
      bot.send_message(message.chat.id, "Приветствую тебя во владениях Королевы Джадис, я могу вам чем-то помочь?")
   
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
      
   if (message.text == "Привет"):
      bot.send_message(message.chat.id, "Здрравствуй Кар!");   
   if (message.text == "Что ты можешь?"):
      bot.send_message(message.chat.id, "Вот скромный список моих возможностей")   
   elif (message.text == "/help"):
      bot.send_message(message.chat.id, "Напиши привет") 
   else:
      bot.send_message(message.chat.id, "Ваша речь мне не знакома. Может вы знаете нарнийский? Напишите /help")    

bot.polling(non_stop=True, interval=0)





# Добавляем тренера
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")  # обучаем базовым фразам

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот с искусственным интеллектом. Чем могу помочь?')

# Обработчик сообщений
def reply(update: Update, context: CallbackContext) -> None:
    response = bot.get_response(update.message.text)
    update.message.reply_text(response)

def main() -> None:
    updater = Updater("YOUR_API_KEY", use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
