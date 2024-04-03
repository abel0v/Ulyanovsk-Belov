import telebot

bot = telebot.TeleBot('6278405915:AAEJyCUHG1OXazuADry8lenCm583KKXxcRo')

to_user = ''


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    if message.text[:6] == '/start':
        bot.send_message(message.from_user.id, f'Напиши сюда, что думаешь об этом человеке и через несколько мгновений '
                                               f'он получит твою валентинку:')

        global to_user
        to_user = message.text[7:]
    else:

        send(to_user, message.text, message)


def send(idd, txt, message):
    bot.send_message(idd, f'тебе пришло анонимное сообщение: \n '' \n {txt}')
    global to_user
    to_user = ''
    bot.send_message(message.from_user.id, 'отправил твоё сообщение!')
    bot.send_message(message.from_user.id, f't.me/ValenAnon_bot?start={message.from_user.id}  \n твоя ссылка')


if __name__ == '__main__':
    bot.infinity_polling()
