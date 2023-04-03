import telebot
import generator
from telebot import types

bot = telebot.TeleBot(token="5612661926:AAGi2cVBLFffgDvhBujxzkIZfWwUQJ2V6fo")

ssubj = None

@bot.message_handler(content_types=["text"])
def start(self):
    global ssubj
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn = [types.KeyboardButton for types.KeyboardButton in generator.sub.keys()]
    markup.add(*btn)
    try:
        if not self.text in commands.keys():
            bot.send_message(self.chat.id, "Я вас не понимаю. Введите /start.", reply_markup=markup)
            bot.register_next_step_handler(self, start)
        else:
            bot.send_message(self.chat.id, commands[self.text], reply_markup=markup)
            bot.register_next_step_handler(self, subj_choice)
            ssubj = self.text
    except:
        print("Error")


def subj_choice(self):
    global ssubj
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = [types.KeyboardButton for types.KeyboardButton in generator.sub.keys()]
    markup.add(*btn)
    if not self.text in commands.keys():
        bot.send_message(self.chat.id, "Я вас не понимаю. Введите название предмета или /start.", reply_markup=markup)
        bot.register_next_step_handler(self, start)
    else:
        ssubj = self.text
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if self.text != "/start":
            btn1 = [types.KeyboardButton for types.KeyboardButton in subj_ch[self.text]]
            markup1.add(*btn1)
            bot.send_message(self.chat.id, commands[self.text], reply_markup=markup1)
            bot.register_next_step_handler(self, send_doc)
        else:
            bot.send_message(self.chat.id, commands[self.text], reply_markup=markup)
            bot.register_next_step_handler(self, subj_choice)


def send_doc(self):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = [types.KeyboardButton for types.KeyboardButton in generator.sub.keys()]
    markup.add(*btn)
    if not self.text in subj_ch[ssubj].keys():
        bot.send_message(self.chat.id, "Я вас не понимаю. Введите название предмета или /start.", reply_markup=markup)
        bot.register_next_step_handler(self, start)
    else:
        try:
            doc = open(subj_ch[ssubj][self.text], "rb")
            print(doc)
            print(subj_ch[ssubj][self.text])
            bot.send_document(self.chat.id, doc, subj_ch[ssubj][self.text])
        except:
            print("He удалось отправить документ.")
        bot.send_message(self.chat.id, "Вот ваш документ.", reply_markup=markup)
        bot.register_next_step_handler(self, subj_choice)

commands = {word: "Выбери класс персонажа." for word in generator.sub.keys()}
commands["/start"] = "Привет, я помогу тебе c учебой. Напиши название предмета, и я скину тебе документацию. Ты можешь в любой момент ввести /start и перезапустить меня."

fun = {word: send_doc for word in generator.sub.keys()}
fun["/start"] = send_doc

subj_ch = {word: {
    "7 класс":f'{generator.sub["Русский"]}.docx', 
    "8 класс":f'{generator.sub["Алгебра"]}.docx', 
    "9 класс": f'{generator.sub["Информатика"]}.docx'
    } for word in generator.sub.keys()}

docs = {word: f"{generator.sub[word]}.docx" for word in generator.sub.keys()}

bot.polling(none_stop=True)