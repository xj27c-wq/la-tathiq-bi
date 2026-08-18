import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🕵️‍♂️ أهلاً بك في «لا تثق بي»!\n\n"
        "اللعبة قيد التجهيز 🔥"
    )

bot.infinity_polling()
