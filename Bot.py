import telebot
import generator
from telebot import types

generator.opendocx()
bot = telebot.TeleBot(token="Token")


@bot.message_handler(content_types=['text'])
def reg(message):
    global commands, fun
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = [types.KeyboardButton for types.KeyboardButton in generator.sub.keys()]
    markup.add(*btn)
        
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
    btn = [types.KeyboardButton for types.KeyboardButton in generator.sub.keys()]
    markup.add(*btn)

    for i in commands.keys():
        if i == message.text:
            try:
                doc = open(docs[i], "rb")
                bot.send_document(message.chat.id, doc, docs[i])
            except:
                pass

            bot.send_message(message.chat.id, commands[i], reply_markup=markup)
            bot.register_next_step_handler(message, fun[i])

    if not message.text in commands.keys():
        bot.send_message(message.chat.id, "He могу прочесть ваше сообщение. Введите предмет повторно или введите /start.")
        bot.register_next_step_handler(message, send_doc)


commands = {word: "Хорошо, вот твой справочник. Можешь выбрать другой предмет." for word in generator.sub.keys()}
commands["/start"] = "Привет, я помогу тебе c учебой. Напиши название предмета, и я скину тебе документацию. Вы можете в любой момент ввести /start и перезапустить меня."

docs = {word: f"{generator.sub[word]}.docx" for word in generator.sub.keys()}

fun = {word: send_doc for word in generator.sub.keys()}
fun["/start"] = send_doc


bot.polling(non_stop=True)