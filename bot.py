import telebot
from telebot import types

bot = telebot.TeleBot(token="TOKEN")


@bot.message_handler(content_types=['text'])
def reg(message):
    global commands, fun
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Алгебра")
    btn2 = types.KeyboardButton("Физика")
    btn3 = types.KeyboardButton("Руссикй")
    btn4 = types.KeyboardButton("Биология")
    markup.add(btn1, btn2, btn3, btn4)
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
    markup.add(btn1, btn2, btn3, btn4)
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

    

commands = {"/start":"Привет, я помогу тебе c учебой. Напиши название предмета, и я скину тебе документацию. Вы можете в любой момент ввести /start и перезапустить меня.",
             "Алгебра": "Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
             "Физика":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
             "Русский":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
             "Биология":"Хорошо, вот твой справочник. Можешь выбрать другой предмет."
}

docs = {
    "Алгебра": "Algebra.pdf",
    "Физика": "Physics.docx",
    "Русский":"Russian.docx",
    "Биология":"Biology.docx"
}

fun = {"/start":send_doc,
       "Алгебра":send_doc,
       "Физика":send_doc,
       "Русский":send_doc,
       "Биология":send_doc
}

bot.polling(non_stop=True)
