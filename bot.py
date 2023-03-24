import telebot
from telebot import types

bot = telebot.TeleBot(token="5612661926:AAFd2ou6nvNmIA8GqzPH-mCQdpQglImNz60")


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
        bot.send_message(message.chat.id, "He могу прочесть ваше сообщение. Введите предмет повторно или введите /start.")
        bot.register_next_step_handler(message, send_doc)

    

commands = {
    "/start":"Привет, я помогу тебе c учебой. Напиши название предмета, и я скину тебе документацию. Вы можете в любой момент ввести /start и перезапустить меня.",
    "Алгебра": "Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "Физика":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "Русский":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "Биология":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "География":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "Литература":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "Геометрия":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "История":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "Обществознание":"Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
    "ОБЖ":"Хорошо, вот твой справочник. Можешь выбрать другой предмет."
}

docs = {
    "Алгебра": "Algebra.pdf",
    "Физика": "Physics.docx",
    "Русский":"Russian.docx",
    "Биология":"Biology.docx",
    "География":"Geography.docx",
    "Литература":"litr.docx",
    "Геометрия":"litr.docx",
    "История":"History.docx",
    "Обществознание":"litr.docx",
    "ОБЖ":"OBJ.docx"
}

fun = {
    "/start":send_doc,
    "Алгебра":send_doc,
    "Физика":send_doc,
    "Русский":send_doc,
    "Биология":send_doc,
    "География": send_doc,
    "Литература": send_doc,
    "Геометрия":send_doc,
    "История":send_doc,
    "Обществознание":send_doc,
    "ОБЖ":send_doc
}

bot.polling(non_stop=True)
