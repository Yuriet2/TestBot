import os
import telebot

BOT_TOKEN = AAHPuORLYqbuet2OQwlx55T4TRHW3ORLn0U

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Bot iniciado correctamente 🎉")

bot.polling(none_stop=True)
