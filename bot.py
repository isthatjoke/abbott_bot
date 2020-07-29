import telebot
from telebot import types

bot = telebot.TeleBot("1337111137:AAELaRg_ixU9Wnx7FYmjXL2TkL1XCAssCUQ")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Рад Вас приветствовать в телеграм-боте транспортного отдела Abbott!")
    bot.send_message(message.from_user.id, "Я могу отправить Вам бланк акта приема-передачи на сдачу или получение"
                                           " автомобиля. Также могу ответить на вопросы по справочному руководству"
                                           " по использованию корпоративного автомобиля")
    bot.send_message(message.from_user.id, "Чем я могу Вам помочь?")


@bot.message_handler(commands=['ss'])
def send_ss_info(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton('Повредили в Ваше отсутствие', callback_data='id_1')
    itembtn2 = types.InlineKeyboardButton('ДТП, второй участник присутствует', callback_data='id_2')
    itembtn3 = types.InlineKeyboardButton('ДТП, второй участник отсутствует', callback_data='id_3')
    itembtn4 = types.InlineKeyboardButton('Треснуло лобовое стекло', callback_data='id_4')
    keyboard.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, 'Выберете категорию страхового случая', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'id_1':
            bot.send_message(call.message.chat.id, "Вы нажали на первую кнопку.")
        if call.data == 'id_2':
            bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")
        if call.data == 'id_3':
            bot.send_message(call.message.chat.id, "Вы нажали на третью кнопку.")
        if call.data == 'id_4':
            bot.send_message(call.message.chat.id, "Вы нажали на четвертую кнопку.")


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
