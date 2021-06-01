from calculator import calculator
from weather import getTemperature
from letter import reletter
#1833116523:AAGcwAYauRWwTPv6hjMPKZLmAVIXH2xYRuw
import telebot
bot = telebot.TeleBot('1833116523:AAGcwAYauRWwTPv6hjMPKZLmAVIXH2xYRuw')
@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.from_user.id,"Привет, Вот что я могу)\n"
                                          "1) Выводить твое смс красивыми буквами для этого введи команду '/letter'\n"
                                          "2) Показывать погоду по выбраному городу для этого введи команду '/weather'\n"
                                          "3) Считать с учетом скобок для этого введи команду '/calcul'\n")

@bot.message_handler(commands=['calcul'])
def calcul(message):
    bot.send_message(message.from_user.id,'Введите строчку с тем что нужно постчитать')
    bot.register_next_step_handler(message, calculPint)


def calculPint(message):
    try:
        bot.send_message(message.from_user.id, str(calculator(message.text)))
    except:
        bot.send_message(message.from_user.id, 'Вы ввели неверную строчку ')
        calcul(message)


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.from_user.id, 'Введите город на английском транслите, пример "moskva"')
    bot.register_next_step_handler(message, temPrint)
def temPrint(message):
    try:
        bot.send_message(message.from_user.id, getTemperature(message.text))
    except:
        bot.send_message(message.from_user.id, 'Вы ввели неверную строчку ')
        weather(message)


@bot.message_handler(commands=['letter'])
def letter(message):
    bot.send_message(message.from_user.id, 'Введите строчку которую нужно вывести красиво(на русском языке)')
    bot.register_next_step_handler(message, letterPrint)
def letterPrint(message):
    try:
        bot.send_message(message.from_user.id, reletter(message.text))
    except:
        bot.send_message(message.from_user.id, 'Вы ввели неверную строчку ')
        letter(message)

@bot.message_handler(commands=['help'])
def help(message):

    bot.send_message(message.from_user.id,"Чтобы узнать мои возможности введите команду '/menu').")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "/start" or message.text.lower == "привет":
        print(message.from_user.id)
        bot.send_message(message.from_user.id,
                         "Привет я бот который может .Если хочешь узнать все мои возможности напиши '/menu'.")

    else:bot.send_message(message.from_user.id, 'Напиши /start')


bot.polling(none_stop=True, interval=0)