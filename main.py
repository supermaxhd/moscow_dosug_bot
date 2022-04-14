import telebot
from telebot import types
import sqlite3

token = '5337943576:AAHg41r6ghSK0d8Z8E6vt8YS8-OVxCUfjLc'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):

    connect = sqlite3.connect('users_bot.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS login_username(id STRING)''')

    connect.commit()


    user_username = message.from_user.id
    cursor.execute(f"SELECT id from login_username WHERE id = {user_username}")
    data = cursor.fetchone()
    if data is None:

        user_username = [message.from_user.username]
        cursor.execute("INSERT INTO login_username VALUES(?);", user_username)
        connect.commit()
    else:
        bot.send_message(message.from_user.id, 'Такой пользователь уже создан.')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 О боте")
    btn2 = types.KeyboardButton("❓ Подобрать досуг")
    btn3 = types.KeyboardButton("💰 Интересные места")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для организации досуговой деятельности населения на территории города Москвы!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text', 'url'])
def func(message):
    if (message.text == "👋 О боте"):
        bot.send_message(message.chat.id, text="Привет, я бот для организации досуговой деятельности населения на территории города Москвы! Я могу подобрать для тебя интересные места, для этого нажми на кнопку 'Подобрать досуг', чтобы я подобрал наиболее подходящие места именно для тебя или на кнопку 'Инетерсные места' ")

    elif (message.text == "❓ Подобрать досуг"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,text='Заполните анекту')
        btn1 = types.KeyboardButton("0 - 7")
        btn2 = types.KeyboardButton("8 - 12")
        btn7 = types.KeyboardButton("13 - 17")
        btn3 = types.KeyboardButton("18 - 24")
        btn4 = types.KeyboardButton("25 - 34")
        btn5 = types.KeyboardButton("35 - 55")
        btn6 = types.KeyboardButton("56 и старше")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn7 ,btn3, btn4, btn5, btn6, back)
        bot.send_message(message.from_user.id, "Выберете ваш возраст", reply_markup=markup)

    elif (message.text == "0 - 7"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Активный 👶")
        btn2 = types.KeyboardButton("Спокойный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас вид досуга.", reply_markup=markup)

    elif (message.text == "8 - 12"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Активный 👶")
        btn2 = types.KeyboardButton("Спокойный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас вид досуга.", reply_markup=markup)

    elif (message.text == "13 - 17"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Активный 👶")
        btn2 = types.KeyboardButton("Спокойный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас вид досуга.", reply_markup=markup)

    elif (message.text == "18 - 24"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Активный 🧔🏻‍♂️")
        btn2 = types.KeyboardButton("Спокойный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас вид досуга.", reply_markup=markup)

    elif (message.text == "25 - 34"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Активный 🧔🏻‍♂️")
        btn2 = types.KeyboardButton("Спокойный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас вид досуга.", reply_markup=markup)

    elif (message.text == "35 - 55"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Активный 🧔🏻‍♂️")
        btn2 = types.KeyboardButton("Спокойный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас вид досуга.", reply_markup=markup)

    elif (message.text == "56 и старше"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Активный 👴🏻")
        btn2 = types.KeyboardButton("Спокойный")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас вид досуга.", reply_markup=markup)

    elif (message.text == "Спокойный"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Парки")
        btn2 = types.KeyboardButton("Театры")
        btn3 = types.KeyboardButton("Музеи")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите интересующее вас место.", reply_markup=markup)

    elif (message.text == "Парки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Парк Горького")
        btn2 = types.KeyboardButton("Зарядье")
        btn3 = types.KeyboardButton("Парк Останкино")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас парк", reply_markup=markup)

    elif (message.text == "Парк Горького"):
        markup = types.InlineKeyboardMarkup()
        park = types.InlineKeyboardButton(text='Парк Горького', url='https://park-gorkogo.com/')
        bot.send_location(message.from_user.id, 55.731430, 37.6033700)
        markup.add(park)
        bot.send_message(message.from_user.id,
                         "Парк Горького – центральный парк столицы, чьи территории посещает более 40 000 человек в будние и 250 000 в выходные и праздничные дни. "
                         "С 2011 года парк задает новые стандарты, став первым парком мирового уровня в России, пространством для отдыха, спорта, танцев и игр на свежем воздухе.", reply_markup=markup)

    elif (message.text == "Зарядье"):
        markup = types.InlineKeyboardMarkup()
        park = types.InlineKeyboardButton(text='Зарядье', url='https://www.zaryadyepark.ru/')
        bot.send_location(message.from_user.id, 55.751487, 37.627086)
        markup.add(park)
        bot.send_message(message.from_user.id,
                         "Зарядье» — современный парк для отдыха, развлечений и получения знаний, созданный международной командой архитекторов, инженеров, ландшафтных дизайнеров и других экспертов.", reply_markup=markup)

    elif (message.text == "Парк Останкино"):
        markup = types.InlineKeyboardMarkup()
        park = types.InlineKeyboardButton(text='Останкино', url='http://park-ostankino.ru/')
        bot.send_location(message.from_user.id, 55.823857, 37.609142)
        markup.add(park)
        bot.send_message(message.from_user.id,
                         "Останкино — один из старейших московских парков, расположенный на территории дворцово-паркового ансамбля XVIII—XIX веков.",
                         reply_markup=markup)

    elif (message.text == "Театры"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Большой театр")
        btn2 = types.KeyboardButton("Московский театр оперетты")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас театр", reply_markup=markup)

    elif (message.text == "Большой театр"):
        markup = types.InlineKeyboardMarkup()
        park = types.InlineKeyboardButton(text='Купить билеты в Большой театр', url='https://bolshoi.ru/timetable/all')
        bot.send_location(message.from_user.id, 55.760178, 37.618575)
        markup.add(park)
        bot.send_message(message.from_user.id,
                         "Государственный академический Большо́й теа́тр Росси́и, или просто Большой театр — один из крупнейших в России и один из самых значительных в мире театров оперы и балета. Комплекс зданий театра расположен в центре Москвы, на Театральной площади.", reply_markup=markup)

    elif (message.text == "Московский театр оперетты"):
        markup = types.InlineKeyboardMarkup()
        park = types.InlineKeyboardButton(text='Купить билеты в Московский театр оперетты', url='https://mosoperetta.ru/bilety/')
        bot.send_location(message.from_user.id, 55.760175, 37.616182)
        markup.add(park)
        bot.send_message(message.from_user.id,
                         "Московский государственный академический теа́тр опере́тты, сокр. назв. «Московская оперетта» или просто Мосоперетта — музыкальный театр в Москве, первый государственный театр оперетты в СССР.", reply_markup=markup)

    elif (message.text == "Музеи"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Музей современного искусства")
        btn2 = types.KeyboardButton("Третьяковская галерея")
        btn3 = types.KeyboardButton("Музей космонавтики")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас музей", reply_markup=markup)

    elif (message.text == "Музей современного искусства"):
        markup = types.InlineKeyboardMarkup()
        park = types.InlineKeyboardButton(text='Купить билеты в Музей современного искусства', url='https://mmoma.ru/about/tickets/')
        bot.send_location(message.from_user.id, 55.767011, 37.614227)
        markup.add(park)
        bot.send_message(message.from_user.id,
                         "Московский музей современного искусства — первый в России государственный музей современного искусства, в коллекциях которого представлены исключительно произведения визуальной культуры ХХ и XXI веков. ", reply_markup=markup)

    elif (message.text == "Третьяковская галерея"):
        markup = types.InlineKeyboardMarkup()
        park = types.InlineKeyboardButton(text='Купить билеты в Третьяковскую галерею', url='https://www.tretyakovgallery.ru/tickets/afisha')
        bot.send_location(message.from_user.id, 55.741556, 37.620028)
        markup.add(park)
        bot.send_message(message.from_user.id,
                         "Третьяко́вская галере́я — московский художественный музей, основанный в 1856 году купцом Павлом Третьяковым. ", reply_markup=markup)

    elif (message.text == "Музей космонавтики"):
        markup = types.InlineKeyboardMarkup()
        park = types.InlineKeyboardButton(text='Купить билеты в музей космонавтики' , url='https://kosmo-museum.ru/')
        bot.send_location(message.from_user.id, 55.823294, 37.639853)
        markup.add(park)
        bot.send_message(message.from_user.id,
                         "Музей космона́втики в Москве — музей космической тематики в стилобате монумента «Покорителям космоса» на Аллее Космонавтов ВДНХ.", reply_markup=markup)

    elif (message.text == "Активный 👶"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Парк аттракционов")
        btn2 = types.KeyboardButton("Спортивные матчи")
        btn3 = types.KeyboardButton("Батутный центр")
        btn4 = types.KeyboardButton("Аквапарк")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Выберите интересующее вас место.", reply_markup=markup)

    elif (message.text == "Активный 🧔🏻‍♂️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Парк аттракционов")
        btn2 = types.KeyboardButton("Спортивные матчи")
        btn3 = types.KeyboardButton("Бары")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите интересующее вас место.", reply_markup=markup)


    elif (message.text == "Активный 👴🏻"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Пешие маршруты")
        btn2 = types.KeyboardButton("Спортивные матчи")
        btn3 = types.KeyboardButton("Бары")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите интересующее вас место.", reply_markup=markup)

    elif (message.text == "Бары"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Ирландский паб Дублинец")
        btn2 = types.KeyboardButton("The Left Bank Pub")
        btn3 = types.KeyboardButton("Политех")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас бар", reply_markup=markup)

    elif (message.text == "Ирландский паб Дублинец"):
        markup = types.InlineKeyboardMarkup()
        way = types.InlineKeyboardButton(text='Ирландский паб Дублинец', url='https://dublinerpub.ru/')
        bot.send_location(message.from_user.id, 55.757672, 37.624529)
        markup.add(way)
        bot.send_message(message.from_user.id, "Приятного вечера!", reply_markup=markup)

    elif (message.text == "The Left Bank Pub"):
        markup = types.InlineKeyboardMarkup()
        way = types.InlineKeyboardButton(text='The Left Bank Pub', url='https://www.tripadvisor.ru/Restaurant_Review-g298484-d12517347-Reviews-The_Left_Bank_Pub-Moscow_Central_Russia.html')
        bot.send_location(message.from_user.id, 55.757775, 37.633592)
        markup.add(way)
        bot.send_message(message.from_user.id, "Приятного вечера!", reply_markup=markup)

    elif (message.text == "Политех"):
        markup = types.InlineKeyboardMarkup()
        way = types.InlineKeyboardButton(text='Политех', url='https://www.tripadvisor.ru/Restaurant_Review-g298484-d13791533-Reviews-Polytech_Lounge_Bar-Moscow_Central_Russia.html')
        bot.send_location(message.from_user.id, 55.758574, 37.629404)
        markup.add(way)
        bot.send_message(message.from_user.id, "Приятного вечера!", reply_markup=markup)

    elif (message.text == "Пешие маршруты"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("По центру Москвы")
        btn2 = types.KeyboardButton("Шумные улицы и бульвары Москвы")
        btn3 = types.KeyboardButton("От Цветного бульвара до Китай-города")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите интересующий вас бар", reply_markup=markup)

    elif message.text == "По центру Москвы":
        bot.send_message(message.from_user.id, "По центру Москвы")
        bot.send_photo(message.chat.id,
                       'https://n1s1.elle.ru/44/77/3b/44773bd5ad8e3ab6a2d108fccbd28c11/727x503_1_da336e8e9055f07b84d748c36434d67a@940x650_0xc35dbb80_6014807221497609956.jpeg')

    elif message.text == "Шумные улицы и бульвары Москвы":
        bot.send_message(message.from_user.id, "Шумные улицы и бульвары Москвы")
        bot.send_photo(message.chat.id,
                       'https://n1s1.elle.ru/17/03/7e/17037e867ca735d7a827c6f4c03092ca/727x503_1_eb3aaf7acac19287a4c5ce1d8dfddc62@940x650_0xc35dbb80_17623187991497610611.jpeg')

    elif message.text == "От Цветного бульвара до Китай-города":
        bot.send_message(message.from_user.id, "От Цветного бульвара до Китай-города")
        bot.send_photo(message.chat.id,
                       'https://n1s1.elle.ru/d0/90/38/d0903816d618e43f4b889692b7441d17/727x503_1_dc031aa9d572ece4b626198085b4c74b@940x650_0xc35dbb80_5533684381497611985.jpeg')

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 О боте")
        btn2 = types.KeyboardButton("❓ Подобрать досуг")
        btn3 = types.KeyboardButton("💰 Интересные места")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Нажмите на интересующую вас кнопку".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Аквапарк"):
        markup = types.InlineKeyboardMarkup()
        way = types.InlineKeyboardButton(text='Аквапарк Мореон🏄🏻‍♂️', url='https://more-on.ru/')
        bot.send_location(message.from_user.id, 55.598274, 37.527370)
        markup.add(way)
        bot.send_message(message.from_user.id, "Многофункциональный комплекс Мореон\n"
                                               "Крупнейший центр водных развлечений в Восточной Европе!", reply_markup=markup)

    elif (message.text == "Спортивные матчи"):
        markup = types.InlineKeyboardMarkup()
        way = types.InlineKeyboardButton(text='Яндекс Афиша🏋🏿‍♂️', url='https://afisha.yandex.ru/moscow/sport')
        markup.add(way)
        bot.send_message(message.from_user.id, "Купить билеты на спортивные события", reply_markup=markup)

    elif (message.text == "Парк аттракционов"):
        markup = types.InlineKeyboardMarkup()
        way = types.InlineKeyboardButton(text='Остров Мечты🎡', url='https://dreamisland.ru/')
        bot.send_location(message.from_user.id, 55.694607, 37.676131 )
        markup.add(way)
        bot.send_message(message.from_user.id, "«Остров мечты» — крупнейший крытый тематический парк развлечений в Европе, включающий в себя торгово-развлекательный комплекс и ландшафтный парк с набережной.", reply_markup=markup)

    elif (message.text == "Батутный центр"):
        markup = types.InlineKeyboardMarkup()
        way = types.InlineKeyboardButton(text='Батутный центр JUSTUP!🤾🏼‍♂️', url='https://just-up.club/')
        bot.send_location(message.from_user.id, 55.787363, 37.530573)
        markup.add(way)
        bot.send_message(message.from_user.id, "«В отличии от обычных батутов, батутные арены JUSTUP! оснащены профессиональными полотнами, позволяющими выдерживать экстремальные нагрузки и обладающими максимальной отдачей. Ваши прыжки будут выше, тренировки эффективней, а удовольствие больше!", reply_markup=markup)

    elif (message.text == "💰 Интересные места"):
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_yes1 = types.KeyboardButton(text='ВДНХ')
        keyboard1.add(key_yes1)
        key_no1 = types.KeyboardButton(text='Екатерининский парк')
        keyboard1.add(key_no1)
        key_no2 = types.KeyboardButton(text='Храм Христа Спасителя')
        keyboard1.add(key_no2)
        key_no3 = types.KeyboardButton(text='Лужков мост')
        keyboard1.add(key_no3)
        back = types.KeyboardButton(text='Вернуться в главное меню')
        keyboard1.add(back)
        bot.send_message(message.from_user.id, text="Вот топ 5 лучших парков для прогулки", reply_markup=keyboard1)

    elif message.text == "ВДНХ":
        bot.reply_to(message, "ВДНХ — крупнейший в Москве выставочный центр. Ежегодно его посещают больше двадцати миллионов человек, а на территории организуют не меньше полутора сотен экспозиций и выставок.")
        bot.send_location(message.from_user.id, 55.826249, 37.637578)
    elif message.text == "Екатерининский парк":
        bot.reply_to(message, "Екатерининский парк — это не только живописные места, но и богатейшая история. До начала XV века на территории парка располагалась красивейшая цепочка различных прудов: все они относились к Неглининским прудам, большинство из которых ныне не сохранились. В XVI веке сюда был перенесён Крестовоздвиженский монастырь, а немного позднее построена церковь Иоанна Воина.")
        bot.send_location(message.from_user.id, 55.784375, 37.620933)
    elif message.text == "Храм Христа Спасителя":
        bot.reply_to(message,"История храма Христа Спасителя во всём, начиная с того места, на котором он возведён, и заканчивая непростой судьбой самого храмового здания, окружена ореолом тайны и мистики.")
        bot.send_location(message.from_user.id, 55.744661, 37.605526)
    elif message.text == "Лужков мост":
        bot.reply_to(message,"Лужков мост любят молодожёны: считается, что выполнение здесь определённого обряда обеспечивает счастье и благополучие в семейной жизни.")
        bot.send_location(message.from_user.id, 55.744419, 37.618486)


    else:
        bot.send_message(message.chat.id, text="Такого я ещё не знаю")


bot.polling(none_stop=True)