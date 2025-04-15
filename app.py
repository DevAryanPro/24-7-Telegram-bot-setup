import telebot

bot = telebot.TeleBot("7398952226:AAGg7yxB7TtoXrJRUptezSirOan2WdGKpL8")

@bot.message_handler(func=lambda _: True)
def reply(message):
    bot.reply_to(message, "I'm alive 24/7!")

bot.polling(none_stop=True)
