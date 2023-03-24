import telebot
import generator
from telebot import types

generator.opendocx()
bot = telebot.TeleBot(token="Token")


@bot.message_handler(content_types=['text'])
def reg(message):
    global commands, fun
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Алгебра")
    btn2 = types.KeyboardButton("Физика")
    btn3 = types.KeyboardButton("Русский")
    btn4 = types.KeyboardButton("Биология")
    btn5 = types.KeyboardButton("География")
    btn6 = types.KeyboardButton("Литература")
    btn7 = types.KeyboardButton("Геометрия")
    btn8 = types.KeyboardButton("История")
    btn9 = types.KeyboardButton("Обществознание")
    btn10 = types.KeyboardButton("ОБЖ")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    for i in commands.keys():
        if i == message.text:
            bot.send_message(message.chat.id, commands[i], reply_markup=markup)
            bot.register_next_step_handler(message, send_doc)
    if not message.text in commands.keys():
        bot.send_message(message.chat.id, "He могу прочесть ваше сообщение. Введите /start.")
        bot.register_next_step_handler(message, reg)


def send_doc(message):
    global commands, fun
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Алгебра")
    btn2 = types.KeyboardButton("Физика")
    btn3 = types.KeyboardButton("Русский")
    btn4 = types.KeyboardButton("Биология")
    btn5 = types.KeyboardButton("География")
    btn6 = types.KeyboardButton("Литература")
    btn7 = types.KeyboardButton("Геометрия")
    btn8 = types.KeyboardButton("История")
    btn9 = types.KeyboardButton("Обществознание")
    btn10 = types.KeyboardButton("ОБЖ")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    for i in commands.keys():
        if i == message.text:
            try:
                doc = open(docs[i], "rb")
                bot.send_document(message.chat.id, doc, docs[i])
            except:
                print("Nope")
                pass
            bot.send_message(message.chat.id, commands[i], reply_markup=markup)
            bot.register_next_step_handler(message, fun[i])
    if not message.text in commands.keys():
        bot.send_message(message.chat.id,
                         "He могу прочесть ваше сообщение. Введите предмет повторно или введите /start.")
        bot.register_next_step_handler(message, send_doc)


commands = {word: "Хорошо, вот твой справочник. Можешь выбрать другой предмет." for word in generator.sub.keys()}

docs = {word: f"{generator.sub[word]}.docx" for word in generator.sub.keys() }

fun = {word: send_doc for word in generator.sub.keys()}

bot.polling(non_stop=True)
