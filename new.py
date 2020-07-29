import telebot
from telebot import types

token = "1335196022:AAEk9MT9PdOsG_fgI9_-dfh88QU2yw8e1bw"
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Рад Вас приветствовать в телеграм-боте транспортного отдела Abbott!")
    bot.send_message(message.from_user.id, "Я могу отправить Вам бланк акта приема-передачи на сдачу или получение"
                                           " автомобиля. Также могу ответить на вопросы по справочному руководству"
                                           " по использованию корпоративного автомобиля")
    bot.send_message(message.from_user.id, "Список доступных команд - /help")

@bot.message_handler(commands=['help'])
def send_act(message):
    bot.send_message(message.chat.id, "/act - получить акт приема или передачи автомобиля")
    bot.send_message(message.chat.id, "/ss - информация по - страховой случай")
    bot.send_message(message.chat.id, "/report - информация по - отчет по пробегу")

@bot.message_handler(commands=['act'])
def send_act(message):
    # создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()

    # добавляем на нее две кнопки
    button1 = types.InlineKeyboardButton(text="Приема", callback_data="get")
    button2 = types.InlineKeyboardButton(text="Сдачи", callback_data="pull")
    keyboard.add(button1)
    keyboard.add(button2)

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Какой акт отправить?", reply_markup=keyboard)

@bot.message_handler(commands=['ss'])
def send_ss_info(message):
    # создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()

    # добавляем на нее две кнопки
    button1 = types.InlineKeyboardButton(text="Повредили в Ваше отсутствие", callback_data="ss_1")
    button2 = types.InlineKeyboardButton(text="ДТП, второй участник присутствует", callback_data="ss_2")
    button3 = types.InlineKeyboardButton(text="ДТП, второй участник отсутствует", callback_data="ss_3")
    button4 = types.InlineKeyboardButton(text="Треснуло лобовое стекло", callback_data="ss_4")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)


    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Выберете категорию страхового случая", reply_markup=keyboard)


@bot.message_handler(text=['ss_2'])
def send_ss_2_info(message):
    # создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()

    # добавляем на нее две кнопки
    button1 = types.InlineKeyboardButton(text="Есть пострадавшие", callback_data="ss_2_yes")
    button2 = types.InlineKeyboardButton(text="Пострадавших нет", callback_data="ss_2_no")
    keyboard.add(button1)
    keyboard.add(button2)

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Есть пострадавшие?", reply_markup=keyboard)


@bot.message_handler(text=['ss_3'])
def send_ss_3_info(message):
    # создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()

    # добавляем на нее две кнопки
    button1 = types.InlineKeyboardButton(text="Есть пострадавшие", callback_data="ss_3_yes")
    button2 = types.InlineKeyboardButton(text="Пострадавших нет", callback_data="ss_3_no")
    keyboard.add(button1)
    keyboard.add(button2)

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Есть пострадавшие?", reply_markup=keyboard)

# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "ss_1":
            bot.send_message(call.message.chat.id, "Не перемещая автомобиль, вызвать сотрудников "
                                                   " ГИБДД/Полиции/Скорой помощи/пожарных по телефону 01 или "
                                                   " с мобильного телефона 112 (Вызов тех или иных служб зависит "
                                                   " от характера повреждений автомобиля, которые поможет вам "
                                                   " определить специалист страхового отдела «Ингосстрах»).\n "
                                                   "Если автомобиль не может перемещаться своим ходом – сообщить "
                                                   " в страховую компанию для вызова эвакуатора.\n"
                                                   " Дождаться приезда сотрудников ГИБДД/Полиции непосредственно "
                                                   " на месте происшествия и зафиксировать "
                                                   " факт повреждения автомобиля.\n"
                                                   " Получить справку, с указанием всех видимых повреждений "
                                                   " Вашего автомобиля.\n Поставить в известность в течение рабочего дня,"
                                                   " оформив отчет о случившемся на "
                                                   "Сервисном Портале/ Транспортный отдел. Обратиться в страховую "
                                                   "компанию")
        if call.data == "ss_2":
            send_ss_2_info(call.message)
        if call.data == "ss_3":
            send_ss_3_info(call.message)
        if call.data == "ss_4":
            bot.send_message(call.message.chat.id, "Вы нажали на четвертую кнопку.")
        if call.data == "ss_2_yes":
            bot.send_message(call.message.chat.id, ".!.")
        if call.data == "ss_2_no":
            bot.send_message(call.message.chat.id, ".!.")
        if call.data == "ss_3_yes":
            bot.send_message(call.message.chat.id, ".!.")
        if call.data == "ss_3_no":
            bot.send_message(call.message.chat.id, ".!.")
        if call.data == "get":
            bot.send_message(call.message.chat.id, "Не забудьте заполнить шапку акта")
            bot.send_message(call.message.chat.id,
                             "https://drive.google.com/file/d/1A6SMTU7wVP6pxe9AbwtusupmZYUXdUdW/view?usp=sharing")
            bot.send_message(call.message.chat.id, "Не пугайтесь, на ноутбуке файл будет выглядеть нормально")
        if call.data == "pull":
            bot.send_message(call.message.chat.id, "Не забудьте заполнить шапку акта")
            bot.send_message(call.message.chat.id,
                             "https://drive.google.com/file/d/1KjfYcq7tUTta4l8XYAv3FkqxXDliU_ib/view?usp=sharing")
            bot.send_message(call.message.chat.id, "Не пугайтесь, на ноутбуке файл будет выглядеть нормально")


@bot.message_handler(commands=['report'])
def send_act(message):
    bot.send_message(message.chat.id, "Сотрудник должен оформить отчет за предыдущий месяц с 08 по 13 число "
                                      " следующего месяца (в случае изменения отчетных дат всегда "
                                      " направляется коммуникация), с указанием пробега автомобиля и "
                                      " количества литров заправленного топлива. \nОтчет оформляется на "
                                      " платформе FleetWeb. Для этого необходимо войти в систему пройдя "
                                      " по ссылке http://online.fleetweb.com/abbott . Логин и пароль аналогичен"
                                      " для входа в систему Oneabbott (SharePoint/PTS). \nВ случае использования "
                                      " топливной карты расходы на приобретение бензина в авансовых отчетах "
                                      " не отражаются. Информационные чеки, которые выдаются на станциях АЗС, "
                                      " к авансовому отчету не прикладываются, а используется только как "
                                      " информационные для сотрудников Компании. \nОтчеты формируются отдельно "
                                      " на каждый автомобиль, бывший в эксплуатации в отчетном месяце. "
                                      " \nВ случае, если в течение месяца Вы использовали несколько автомобилей, "
                                      " то будут сформированы отдельные отчеты на каждый автомобиль, соответственно, "
                                      " заполнить необходимо будет каждый отчет.\n Если Вам пришло письмо о блокировке"
                                      " топливной карты, проверьте пожалуйста заполнение отчета по пробегу в системе"
                                      " fleetweb (обязательное наличие галочки 'ПЛ подтвержден'. Для разблокировки"
                                      " топливной карты необходимо составить запрос на сервисном портале.")

bot.polling(none_stop=False, interval=0, timeout=5)

"""
help - список команд
act - получить акт приема или передачи автомобиля
ss - страховой случай
report - отчет по пробегу
"""