import telebot
from telebot import types

TOKEN = '5186940926:AAHK7YgxaCwVHgtuWYFgp65fRzlZIiptybI'

bot = telebot.TeleBot(TOKEN)

user_data = {}
regions = ["Республика Узбекистан", "город Ташкент", "Андижанская область", "Бухарская область", "Джизакская область",
           "Кашкадарьинская область", "Наманганская область", "Навоийская область", "Самаркандская область",
           "Сурхандарьинская область", "Сырдарьинская область", "Ташкентская область", "Ферганская область",
           "Хорезмская область", "Республика Каракалпакстан"]

category = ["Культурно массовая работа", "Физическая культура и спорт", "Оздаровление"]

sub_category_culture = ["Билеты в театры", "Экскурсии", "Конкурсы"]
sub_category_sport = ["Абонементы в бассейн", "Абонементы в тренажёрный зал", "Турниры по волейболу, баскетболу и т.д.",
                      "Выездные соревнования"]
sub_category_health = ["Путёвки в санатории", "Путёвки в дома отдыха", "Детские оздаровительные лагеря"]

final_select_culture_theatre = []
final_select_culture_tours = []
final_select_culture_competitions = []
final_select_sport_pool = [["спорт комплекс \"Saxovat sport servis\"", "по усмотрению", "1 месяц",
                            "55.000 - 462.000 сум", "1. Оздаровительные группы и группы начального обучения плаванию"
                                                    "\n - дети от 7 до 15 лет - 360.000 сум (абонемент)"
                                                    "\nнаполняемость - 18 - 20 человек\nкол-во занятий - 12"
                                                    "\n - взрослые от 15 и выше - 462.000 сум (абонемент)"
                                                    "\nнаполняемость - 20 - 22 человек\nкол-во занятий - 12"
                                                    "\n2. Индивидуальные занятия для не умеющих плавать"
                                                    "\n - дети от 4.5 до 15 лет - 55.000 сум (разовое)"
                                                    "\nнаполняемость - 1 - 4 человек\nкол-во занятий - неограничено"
                                                    "\n - взрослые от 15 и старше - 70.000 сум (разовое)"
                                                    "\nнаполняемость - 1 - 4 человек\nкол-во занятий - неограничено"
                                                    "\n3. Разовое посещение занятий"
                                                    "\nцена - 60.000 сум (разовое)"
                                                    "\nнаполняемость - 20 - 22 человек\nкол-во занятий - неограничено"
                                                    "\n4. Оздаровительные услуги (сауна)"
                                                    "\nцена - 160.000 сум"
                                                    "\nнаполняемость - до 6 человек\nвремя занятий - 1 час"]]
final_select_sport_gym = []
final_select_sport_tournaments = []
final_select_sport_competitions = []
final_select_health_sanatoriums = [["санатория \"Абу Али Ибн Сино\"", "по усмотрению", "12 дней",
                                    "1.920.000 - 4.200.000 сум", "кардиология, опорно-двигательная, неврология"],
                                   ["санатория \"Ботаника\"", "по усмотрению", "12 дней",
                                    "3.180.000 - 5.040.000 сум", "кардиология, терапия, неврология"],
                                   ["санатория \"Бўстон\"", "по усмотрению", "12 дней",
                                    "3.245.000 - 3.762.000 сум", "кардиология, опорно-двигательная, неврология"
                                                                 "гинекология"],
                                   ["санатория \"Косонсой\"", "по усмотрению", "12 дней",
                                    "2.811.000 - 2.382.000 сум", "терапия, неврология, гинекология"],
                                   ["санатория \"Кўхинур\"", "по усмотрению", "12 дней",
                                    "3.756.000 - 4.425.000 сум", "кардиология, терапия, неврология"],
                                   ["санатория \"Қашқадарё сохили\"", "по усмотрению", "12 дней",
                                    "2.640.000 - 3.192.000 сум", "пищеварительная, неврология, гинекология, кардиология"],
                                   ["санатория \"Олтинсой\"", "по усмотрению", "12 дней",
                                    "1.980.000 - 2.640.000 сум", "терапия, неврология"],
                                   ["санатория \"Ситораи Мохи Хоса\"", "по усмотрению", "12 дней",
                                    "2.640.000 - 3.300.000 сум", "терапия, неврология, гинекология, урология"],
                                   ["санатория \"Термиз Марвариди\"", "по усмотрению", "12 дней",
                                    "2.736.000 - 3.900.000", "кардиология, опорно-двигательная, неврология"],
                                   ["санатория \"Турон\"", "по усмотрению", "12 дней",
                                    "2.292.000 - 5.659.000 сум", "кардиология, неврология, урология"],
                                   ["санатория \"Умид гулшани\"", "по усмотрению", "12 дней",
                                    "3.000.000 - 3.720.000 сум", "гинекология, урология, терапия, неврология"],
                                   ["санатория \"Хавотоғ гулшани\"", "по усмотрению", "12 дней",
                                    "2.640.000 - 2.851.000 сум", "кардиология, опорно-двигательная, неврология"],
                                   ["санатория \"Хонқа\"", "по усмотрению", "12 дней",
                                    "2.160.000 - 2.880.000 сум", "кардиология, опорно-двигательная, неврология, "
                                                                 "гинекология"],
                                   ["санатория \"Хўжаипок\"", "по усмотрению", "12 дней",
                                    "3.029.000 - 3.677.000 сум", "кардиология, опорно-двигательная, неврология, терапия"],
                                   ["санатория \"Чинобод\"", "по усмотрению", "12 дней",
                                    "3.204.000 - 5.364.000 сум", "пищеварительная, эндокринология, гинекология"],
                                   ["санатория \"Чинобод Плаза\"", "по усмотрению", "12 дней",
                                    "5.800.000 - 12.800.000 сум", "пищеварительная, эндокринология, гинекология, "
                                                                  "неврология"],
                                   ["санатория \"Чортоқ\"", "по усмотрению", "12 дней",
                                    "2.640.000 - 2.940.000 сум", "опорно-двигательная, кардиология, терапия, "
                                                                 "неврология, гинекология"],
                                   ["санатория \"Чимён\"", "по усмотрению", "12 дней",
                                    "2.468.000 - 3.607.000 сум", "кардиология, гинекология, опорно-двигательная, "
                                                                 "неврология"],
                                   ["санатория \"Янгиер\"", "по усмотрению", "12 дней",
                                    "3.204.000 - 5.508.000 сум", "кардиология, опорно-двигательная, неврология, "
                                                                 "урология, геникология"],
                                   ["санатория \"Зомин\"", "по усмотрению", "10 дней",
                                    "3.032.000 сум - 5.453.000 сум", "дыхательные"],
                                   ["санатория \"Оқ-Тош\"", "по усмотрению", "10 дней",
                                    "2.645.000 - 4.960.000 сум", "дыхательные"],
                                   ["санатория \"Оқ-Тош Шабода\"", "по усмотрению", "10 дней",
                                    "2.800.000 - 4.200.000 сум", "дыхательные"],
                                   ["санатория \"Сангардек\"", "по усмотрению", "10 дней",
                                    "350.000 сум (1кун)", "отдых"]]
final_select_health_rest = [["дом отдыха \"Ахмад Ал_Фарғоний\"", "по усмотрению", "1 день", "180.000 сум",
                             "отдых"]]
final_select_health_camp = []


class User:
    def __init__(self, name):
        self.name = name
        self.region = ''
        self.category = ''
        self.sub_category = ''
        self.final_select = ''
        self.final_select_date = ''
        self.final_select_duration = ''
        self.final_select_price = ''
        self.final_select_add = ''
        self.overall_final_select_list = []
        self.temp_final_select_list = []


@bot.message_handler(commands=['start'])
def start(message):
    start_message = bot.send_message(message.chat.id, "Добро пожаловать!\nДля начала работы введите ваше имя:")
    bot.register_next_step_handler(start_message, get_name)


def get_name(message):
    try:
        chat_id = message.chat.id
        name_text = message.text
        user = User(name_text)
        user_data[chat_id] = user
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in regions:
            button = types.KeyboardButton(i)
            markup.add(button)
        get_name_message = bot.send_message(chat_id, f"Отлично <b><i>{user.name}</i></b>!\nВыберите свой регион",
                                            parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(get_name_message, get_region)
    except Exception as e:
        print(e)
        bot.send_message(message, "Неправильная команда!")


def get_region(message):
    try:
        chat_id = message.chat.id
        region_text = message.text
        if region_text not in regions:
            get_region_message = bot.send_message(chat_id, f"Пожалуйста выберите один из кнопок ниже!",
                                                  parse_mode='html')
            bot.register_next_step_handler(get_region_message, get_region)
            return
        user = user_data[chat_id]
        user.region = region_text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in category:
            button = types.KeyboardButton(i)
            markup.add(button)
        get_region_message = bot.send_message(chat_id, f"Ваш выбор: <b><i>{user.region}</i></b>"
                                                       f"\nВыберите один из категорий ниже:",
                                              parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(get_region_message, get_category)
    except Exception as e:
        print(e)
        bot.send_message(message, "Неправильная команда!")


def get_category(message):
    try:
        chat_id = message.chat.id
        category_text = message.text
        if category_text not in category:
            get_category_message = bot.send_message(chat_id, f"Пожалуйста выберите один из кнопок ниже!",
                                                    parse_mode='html')
            bot.register_next_step_handler(get_category_message, get_category)
            return
        user = user_data[chat_id]
        user.category = category_text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        if category_text == "Культурно массовая работа":
            for i in sub_category_culture:
                button = types.KeyboardButton(i)
                markup.add(button)
        elif category_text == "Физическая культура и спорт":
            for i in sub_category_sport:
                button = types.KeyboardButton(i)
                markup.add(button)
        elif category_text == "Оздаровление":
            for i in sub_category_health:
                button = types.KeyboardButton(i)
                markup.add(button)
        get_category_message = bot.send_message(chat_id, f"Ваш выбор: <b><i>{user.category}</i></b>"
                                                         f"\nВыберите один из подкатегорий ниже:", parse_mode='html',
                                                reply_markup=markup)
        bot.register_next_step_handler(get_category_message, get_sub_category)
    except Exception as e:
        print(e)
        bot.send_message(message, "Неправильная команда!")


def get_sub_category(message):
    try:
        chat_id = message.chat.id
        sub_category_text = message.text
        overall_sub_category = sub_category_culture + sub_category_sport + sub_category_health
        if sub_category_text not in overall_sub_category:
            get_sub_category_message = bot.send_message(chat_id, f"Пожалуйста выберите один из кнопок ниже!",
                                                        parse_mode='html')
            bot.register_next_step_handler(get_sub_category_message, get_sub_category)
            return
        user = user_data[chat_id]
        user.sub_category = sub_category_text
        overall_final_select = []
        temp_final_select = []
        answer_text = ""
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
        if sub_category_text == "Билеты в театры":
            if len(final_select_culture_theatre) > 0:
                for i in final_select_culture_theatre:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_culture_theatre
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Экскурсии":
            if len(final_select_culture_tours) > 0:
                for i in final_select_culture_tours:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_culture_tours
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Конкурсы":
            if len(final_select_culture_competitions) > 0:
                for i in final_select_culture_competitions:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_culture_competitions
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Абонементы в бассейн":
            if len(final_select_sport_pool) > 0:
                for i in final_select_sport_pool:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_sport_pool
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Абонементы в тренажёрный зал":
            if len(final_select_sport_gym) > 0:
                for i in final_select_sport_gym:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_sport_gym
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html', reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Турниры по волейболу, баскетболу и т.д.":
            if len(final_select_sport_tournaments) > 0:
                for i in final_select_sport_tournaments:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_sport_tournaments
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Выездные соревнования":
            if len(final_select_sport_competitions) > 0:
                for i in final_select_sport_competitions:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_sport_competitions
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Путёвки в санатории":
            if len(final_select_health_sanatoriums) > 0:
                for i in final_select_health_sanatoriums:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_health_sanatoriums
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Путёвки в дома отдыха":
            if len(final_select_health_rest) > 0:
                for i in final_select_health_rest:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_health_rest
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас раздел:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        elif sub_category_text == "Детские оздаровительные лагеря":
            if len(final_select_health_camp) > 0:
                for i in final_select_health_camp:
                    button = types.KeyboardButton(i[0])
                    temp_final_select = final_select_health_camp
                    overall_final_select.append(i[0])
                    markup.add(button)
                answer_text = f"Ваш выбор: <b><i>{user.sub_category}</i></b>\nВыберите интересующий вас предложение:"
            else:
                answer_text = "Извините, но по данному запросу нет соответствующих предложений.\nПрийдётся начать " \
                              "с начала /start"
                remove_markup = types.ReplyKeyboardRemove(selective=False)
                get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                            reply_markup=remove_markup)
                bot.register_next_step_handler(get_sub_category_message, start)
                return
        user.temp_final_select_list = temp_final_select
        user.overall_final_select_list = overall_final_select
        get_sub_category_message = bot.send_message(chat_id, answer_text, parse_mode='html',
                                                    reply_markup=markup)
        bot.register_next_step_handler(get_sub_category_message, get_final_select)
    except Exception as e:
        print(e)
        bot.send_message(message, "Неправильная команда!")
        bot.register_next_step_handler(message, get_sub_category)


def get_final_select(message):
    try:
        chat_id = message.chat.id
        final_select_text = message.text
        user = user_data[chat_id]
        if final_select_text not in user.overall_final_select_list:
            get_final_select_message = bot.send_message(chat_id, f"Пожалуйста выберите один из кнопок ниже!",
                                                        parse_mode='html')
            bot.register_next_step_handler(get_final_select_message, get_final_select)
            return
        parent_list = user.temp_final_select_list
        user.final_select = final_select_text
        parent_index = 0
        children_index = 0
        for children_list in parent_list:
            if final_select_text in children_list:
                parent_index = parent_list.index(children_list)
                children_index = children_list.index(final_select_text)
        select_date = parent_list[parent_index][children_index + 1]
        select_duration = parent_list[parent_index][children_index + 2]
        select_price = parent_list[parent_index][children_index + 3]
        select_add = parent_list[parent_index][children_index + 4]
        user.final_select_date = select_date
        user.final_select_duration = select_duration
        user.final_select_price = select_price
        user.final_select_add = select_add
        bot.send_message(chat_id, f"<b>Регион:</b> <i>{user.region}</i>\n<b>Категория:</b> "
                                  f"<i>{user.category}</i>\n<b>Суб-категория:</b> <i>{user.sub_category}</i>"
                                  f"\n<b>Наименование:</b> "
                                  f"<i>{user.final_select}</i>\n<b>Дата начала:</b> <i>{user.final_select_date}</i>\n<b"
                                  f">Длительность:</b> <i>{user.final_select_duration}</i>\n<b>Цена:</b> "
                                  f"<i>{user.final_select_price}</i>\n<b>Дополнительно:</b>\n"
                                  f"<i>{user.final_select_add}</i>"
                                  f"\n\n*********************************\n"
                                  f"<i>Члены профсоюза оплачивают 45% от стоимости путёвки."
                                  f"\nЖелающим приобрести путёвки необходимо подать заявку в профком Узгидромета</i>"
                                  f"\n\n- чтобы начать сначала введите команду /start",
                         parse_mode='html')
    except Exception as e:
        print(e)
        bot.send_message(message, "Неправильная команда!")


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.infinity_polling()
