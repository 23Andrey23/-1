import telebot
from config import keys, TOKEN
from extensions import Convert, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите слелующие действия: \n<имя валюты>\n<в какую валюту перевести>\n<количество переводимой валюты>\nКоманды этого бота:/start  /help  /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Введенные вами параметры не корректны')

        quote, base, amount = values
        total_base = Convert.get_price(quote, base, amount)

    except APIException as error:
        bot.reply_to(message, f'Ошибка пользователя:\n{error}')
    except Exception as error:
        bot.reply_to(message, f'Не удалось обработать команду\n{error}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()

