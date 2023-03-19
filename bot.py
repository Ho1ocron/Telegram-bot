import telebot

bot = telebot.TeleBot(token="6060505951:AAF8PitSfd2nmcdpHcEikBCEgK1D6r79f8c")


@bot.message_handler(content_types=['text'])
def reg(message):
    global commands, fun
    for i in commands.keys():   
        if i == message.text:
            bot.send_message(message.chat.id, commands[i])
            bot.register_next_step_handler(message, send_doc)


def send_doc(message):
    global commands, fun
    for i in commands.keys():
        if i == message.text:
            try:
                doc = open(docs[i], "rb")
                bot.send_document(message.chat.id, doc, docs[i])
            except:
                pass    
            bot.send_message(message.chat.id, commands[i])
            bot.register_next_step_handler(message, fun[i])

    

commands = {"/start":"Привет, я помогу тебе c учебой. Напиши название предмета, и я скину тебе документацию. /doc, /doc1",
             "/doc": "Хорошо, вот твой справочник. Можешь выбрать другой предмет.",
             "/doc1":"Хорошо, вот твой справочник. Можешь выбрать другой предмет."
}

docs = {
    "/doc": "wasd.docx",
    "/doc1": "sad.docx"
}

fun = {"/start":send_doc,
       "/doc":send_doc,
       "/doc1":send_doc
}

bot.polling(non_stop=True)
