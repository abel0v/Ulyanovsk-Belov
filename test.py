import telebot

bot = telebot.TeleBot('6278405915:AAEJyCUHG1OXazuADry8lenCm583KKXxcRo')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
