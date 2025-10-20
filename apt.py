import telebot
from telebot import types

bot = telebot.TeleBot('8179759241:AAGrBMXOPBOrqRPpPHp1U69UgsXbvzNDKYM')

@bot.message_handler(commands=['start'])
def get_text_messages(message):
   
   if (message.text == "/start"):
      bot.send_message(message.chat.id, "Приветствую тебя во владениях Королевы Джадис, я могу вам чем-то помочь?")
   
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
      
   if (message.text == "Привет"):
      bot.send_message(message.chat.id, "Здрравствуй Кар!")   
   if (message.text == "Что ты можешь?")
      bot.send_message(message.chat.id, "Вот скромный список моих возможностей")   
   elif (message.text == "/help"):
      bot.send_message(message.chat.id, "Напиши привет") 
   else:
      bot.send_message(message.chat.id, "Ваша речь мне не знакома. Может вы знаете нарнийский? Напишите /help")    

bot.polling(non_stop=True, interval=0)