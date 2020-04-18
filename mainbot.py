################################################################################################################################################################################################
###                                                                                      Foresti 2020                                                                                      ####
################################################################################################################################################################################################
#Библиотекaaaaaaaaaaa
import configbot
from configbot import admin_id
import time
import telebot
from telebot import types
import pyowm
from colorama import init, Fore
import bs4
import requests
import COVID19Py
################################################################################################################################################################################################
###                                                                                          API                                                                                             ###
################################################################################################################################################################################################
#Токен тех.работы  ([ВНИМАНИЕ!!!] За комментировать след. TOKEN. В случае активации этого)
# bot = telebot.TeleBot(configbot.TEST)

#Токен
bot = telebot.TeleBot(configbot.TOKEN)
covid19 = COVID19Py.COVID19()
################################################################################################################################################################################################
###                                                                                         Теримнал                                                                                         ###
################################################################################################################################################################################################
def star(call, callans):
    init()
    print(Fore.YELLOW)
    print("\n---------Foresti_CMD---------")
    print(time.ctime(int(time.time())), "\nUSER: @{0}\
                                         \nИмя: {1}\
                                         \nФамилия: {2}\
                                         \nID: {3}\n\
                                         \nПоставил звезд:".format(call.from_user.username, call.from_user.first_name,
                                                                   call.from_user.last_name,
                                                                   str(call.from_user.id)))
    print(callans)
    print("-----------------------------")
    print(Fore.WHITE)

def func(call, ansfunc):
    init()
    print(Fore.CYAN)
    print("\n---------Foresti_CMD---------")
    print(time.ctime(int(time.time())), "\nUSER: @{0}\
                                         \nИмя: {1}\
                                         \nФамилия: {2}\
                                         \nID: {3}\n".format(call.from_user.username, call.from_user.first_name,
                                                                   call.from_user.last_name,
                                                                   str(call.from_user.id)))
    print("->", ansfunc)
    print("-----------------------------")
    print(Fore.WHITE)

def txt(message, answer):
    init()
    print(Fore.GREEN)
    print("\n---------Foresti_CMD---------")
    print(time.ctime(int(time.time())), "\nUSER: @{0}\
                                         \nИмя: {1}\
                                         \nФамилия: {2}\
                                         \nID: {3}\n\
                                         \nСообщение: {4}".format(message.from_user.username,
                                                                   message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print("->", answer, "<-")
    print("-----------------------------")
    print(Fore.WHITE)
################################################################################################################################################################################################
#Бан Лист
banlist = [840599371]
################################################################################################################################################################################################
###                                                                                           Команды                                                                                        ###
################################################################################################################################################################################################
###                                      Команда /start                                      ###
################################################################################################
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.delete_message(message.chat.id, message.message_id)#Удалить сообщение

    if message.from_user.id == banlist: #Бан юзеров
        delet = types.ReplyKeyboardRemove()
        file_id = 'CAACAgIAAxkBAAJJa16aMaDA7qpL2prtgpPnZ7vGNVe0AAJ-BQACztjoC9E5b_hSh1A0GAQ'
        bot.send_sticker(message.chat.id, file_id)
        bot.send_message(message.chat.id, 'ВЫ БЫЛИ ЗАБАНЕНЫ!', reply_markup=delet)
    else:
        print("\n---------Foresti_CMD---------")                                                                #Терминал
        print(time.ctime(int(time.time())), "\nUSER: @{0}\
                                             \nИмя: {1}\
                                             \nФамилия: {2}\
                                             \nID: {3}\n".format(message.from_user.username,
                                                                       message.from_user.first_name,
                                                                       message.from_user.last_name,
                                                                       str(message.from_user.id)))
        print("Запустил бота!")
        print("-----------------------------")

        # Стикер
        file_id = 'CAACAgIAAxkBAAJJaV6aMWT4JQbsYEVZZ7VivtL_YV6PAAJtBQACztjoC70P1nRDCpMcGAQ'
        bot.send_sticker(message.chat.id, file_id)
        #Сообщение /start
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, ваш помощник в социальных сетях.".format(message.from_user, bot.get_me()), parse_mode='html')
        mainkeyboard(message)
################################################################################################
###                                      Команда /help                                       ###
################################################################################################
@bot.message_handler(commands=['help'])
def help(message):
    file_id = 'CAACAgIAAxkBAAJJbV6aMez2goOqWyyrNg06bZeg8xmXAAKmBQACztjoC8vKTTQSsWS3GAQ'
    bot.send_sticker(message.chat.id, file_id)
    bot.send_message(message.chat.id, "Если у вас возникли вроблемы. \nНажмите на /restart. \nЕсли не сработала обратитесь к администратору в разделе \n*Обратная* *связь* 📞", parse_mode='markdown')
################################################################################################
###                                  Команда /restart                                        ###
################################################################################################
@bot.message_handler(commands=['restart'])
def stop(message):
    pass
    delete = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Система была перезагружена!", reply_markup=delete)
    mainkeyboard(message)
################################################################################################################################################################################################
#                                                                                           Короновирус
################################################################################################################################################################################################
def cvd_panel(message):
    global cvd_sticker
    markup = types.InlineKeyboardMarkup(row_width=2)

    ru = types.InlineKeyboardButton("Россия🇷🇺", callback_data='ru_cvd')
    kz = types.InlineKeyboardButton("Казахстан🇰🇿", callback_data='kz_cvd')
    bl = types.InlineKeyboardButton("Беларусия🇧🇾", callback_data='bl_cvd')
    uk = types.InlineKeyboardButton("Украина🇺🇦", callback_data='uk_cvd')
    world = types.InlineKeyboardButton("Мир 🌏", callback_data='world_cvd')
    us = types.InlineKeyboardButton("США 🇺🇸", callback_data='us_cvd')
    it = types.InlineKeyboardButton("Италия 🇮🇹", callback_data='it_cvd')
    uz = types.InlineKeyboardButton("Узбекистан 🇺🇿", callback_data='uz_cvd')
    pl = types.InlineKeyboardButton("Польша 🇵🇱", callback_data='pl_cvd')

    markup.add(world)
    markup.add(ru, kz)
    markup.add(bl, uk)
    markup.add(us, it)
    markup.add(uz, pl)

    file_id = 'CAACAgIAAxkBAAJHr16XGp5ZZwRzJjyw7ZuejrB4sHE8AALyAQACVp29CgqJR4ysf4fyGAQ'
    cvd_sticker = bot.send_sticker(message.chat.id, file_id)
    bot.send_message(message.chat.id, 'Выберите страну:', reply_markup=markup)
################################################################################################################################################################################################
###                                                                                            Функция                                                                                       ###
################################################################################################################################################################################################
###                                     FUNC ГЛАВНЫЙ ПАНЕЛЬ                                  ###
################################################################################################
def mainkeyboard(message):
    key = types.ReplyKeyboardMarkup(resize_keyboard=True)

    next = types.KeyboardButton("[Далее]")
    social = types.KeyboardButton("Соц.Сети📱")
    games = types.KeyboardButton("Игры 🎮")
    weather = types.KeyboardButton("Погода ⛅️")
    anekdot = types.KeyboardButton("Анекдот😂")
    virus = types.KeyboardButton("COVID-19🦠")

    key.row(social)
    key.row(games, anekdot)
    key.row(weather, virus)
    key.row(next)

    bot.send_message(message.chat.id, '`Выберите` `интересующий` `вас` `раздел:`', reply_markup=key, parse_mode='markdown', disable_web_page_preview=True)
################################################################################################
###                                     FUNC СЛЕД СТР                                        ###
################################################################################################
def next(message):
    types.ReplyKeyboardRemove()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    versionbb = types.KeyboardButton("Версия БОТа 🤖")
    creator = types.KeyboardButton("Создатели 👨🏻‍💻")
    callback = types.KeyboardButton("Обратная связь 📞")
    # pp = types.KeyboardButton("Телеграмм бот от наших друзей")
    back = types.KeyboardButton("[Назад]")
    review = types.KeyboardButton("Оставить отзыв ⭐️")

    markup.add(versionbb, creator)
    markup.add(review, callback)
    # markup.add(pp)
    markup.add(back)
    bot.send_message(message.chat.id, '`Выберите` `интересующий` `вас` `раздел:`', reply_markup=markup, parse_mode='markdown')
################################################################################################
###                                      FUNC CALLBACK                                         ###
################################################################################################
def callback(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJJb16aMjJL6WR31YWAW329kHz2vCHbAAKrBQACztjoC3vwAAGsZfJ5PxgE')
    bot.send_message(message.chat.id, 'Если у вас возникли проблемы, напишите на почту:\nnazarex1020@gmail.com или же напишите [сюда](https://t.me/nagiez)', parse_mode='markdown', disable_web_page_preview=True)
################################################################################################
###                                      FUNC CREATOR                                        ###
################################################################################################
def creator(message):
    bot.send_message(message.chat.id, 'Данный телеграмм бот был создан командой *Foresti* *Team* \
                                                                                                \n\
                                                                                                \n*Разработчик:* `Нурмухаммед` `Бостан` \
                                                                                                \n*Аналитик:* `Михаил` `Сухов`\
                                                                                                \n*Тестировщик*: `Илья` `Конощенок`\
                                                                                                \n*Менеджер* *проекта:* `Илья` `Бугаёв`',
                                                                                                parse_mode='markdown')

def version(message):
    bot.send_message(message.chat.id, 'Версия `1.7.10-b`', parse_mode='markdown')
################################################################################################
###                                      FUNC SOCIAL                                         ###
################################################################################################
def call_social(message):

    markup = types.InlineKeyboardMarkup(row_width=2)

    video_in_audio_yt = types.InlineKeyboardButton("Конвертация аудио в видео из YouTube", callback_data='v_i_a_yt')
    dwnl_video_yt = types.InlineKeyboardButton("Скачать видео из YouTube", callback_data='d_v_yt')
    dwnl_photo_ins = types.InlineKeyboardButton("Скачать фото из Instagram", callback_data='d_p_ins')
    dwnl_video_ins = types.InlineKeyboardButton("Скачать видео из Instagram", callback_data='d_v_ins')

    markup.add(video_in_audio_yt)
    markup.add(dwnl_video_yt)
    markup.add(dwnl_photo_ins)
    markup.add(dwnl_video_ins)

    file_id = 'CAACAgIAAxkBAAJJcV6aMmuDvoXyeIz9XG6SYfEAAQjrBwACjQUAAs7Y6AsiezOh7cvX6BgE'
    bot.send_sticker(message.chat.id, file_id)
    bot.send_message(message.chat.id, 'Список функционала:', reply_markup=markup)
################################################################################################
###                                     FUNC АНЕКДОТ                                         ###
################################################################################################
def getanekdot():
    z=''
    s=requests.get('http://anekdotme.ru/random')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.anekdot_text')
    for x in p:
        s=(x.getText().strip())
        z=z+s+'\n\n'
    return s
################################################################################################
###                                      FUNC WEATHER                                        ###
################################################################################################
def weather_owm(call, weather_city, weather_city1, weather_city2):
    owm = pyowm.OWM('27d057065c7fb12eb132fe31b42c2195', language = "ru")
    observation = owm.weather_at_place(weather_city)
    w = observation.get_weather()

    temp = w.get_temperature('celsius') ["temp"]
    speed = w.get_wind() ["speed"]
    tempmin = w.get_temperature('celsius') ["temp_min"]
    tempmax = w.get_temperature('celsius') ["temp_max"]

    if temp < -20:
        answer_weather = "\n\n[Лучше сидеть дома!]"
    elif temp < -10:
        answer_weather = "\n\n[На улице мороз, возми перчатки!]"
    elif temp < 0:
        answer_weather = "\n\n[На улице очень холодно! Не забудь шапку!]"
    elif temp < 15:
        answer_weather = "\n\n[Сейчас холодно, одевайся потеплее.]"
    elif temp < 35:
        answer_weather = "\n\n[Температура норм, надевай что угодно.]"
    else:
        answer_weather = "\n\n[На улице жара]"
        file_id = 'CAACAgIAAxkBAAI_5V6NxC18AVgHWhOUDJeVPl1wiOJvAAICAwACusCVBTRFBuRNlNodGAQ'
        bot.send_sticker(call.message.chat.id, file_id)

    bot.send_message(call.message.chat.id,"В городе " + weather_city1 + " сейчас: " + w.get_detailed_status() + "\nТекущая температура в " + weather_city2 + " составляет: " + str(temp)+ " °C." + "\nMin/Max = " + str(tempmin) + " / " + str(tempmax) + " °C" + " \nСкорость ветра составляет: " + str(speed) + " м/с" + str(answer_weather))
    bot.delete_message(call.message.chat.id, call.message.message_id)
################################################################################################################################################################################################
###                                                                                              ТЕКСТ                                                                                       ###
################################################################################################################################################################################################
@bot.message_handler(content_types=['text'])
def ansbutton(message):
    global call_weather_message
    if message.chat.type == 'private':
        if message.from_user.id == banlist:
            bot.delete_message(message.chat.id, message.message_id)
            delet = types.ReplyKeyboardRemove()
            file_id = 'CAACAgIAAxkBAAI2qF54r4eaZHe6ZZyCBzJg2POqbRWhAAItAQACWQMDAAEt9hslJkzrsRgE'
            bot.send_sticker(message.chat.id, file_id)
            bot.send_message(message.chat.id, 'ВЫ БЫЛИ ЗАБАНЕНЫ!', reply_markup=delet)
        else:
            ################################################################################################
            ###                                          Панель                                          ###
            ################################################################################################
            if message.text == 'Погода ⛅️':
                markup = types.InlineKeyboardMarkup(row_width=2)
                piter = types.InlineKeyboardButton("Санкт-Петербург, РФ 🇷🇺", callback_data='piter1')
                moscow = types.InlineKeyboardButton("Москва, РФ 🇷🇺", callback_data='moscow1')
                kazan = types.InlineKeyboardButton("Казань, РФ 🇷🇺", callback_data='kazan1')
                ekb = types.InlineKeyboardButton("Екатеринбург, РФ 🇷🇺", callback_data='ekb1')
                nov = types.InlineKeyboardButton("Новосибирск, РФ 🇷🇺", callback_data='nov1')
                kalin = types.InlineKeyboardButton("Калининград, РФ 🇷🇺", callback_data='kalin1')
                shym = types.InlineKeyboardButton("Шымкент, РК 🇰🇿", callback_data='shym1')
                alm = types.InlineKeyboardButton("Алматы, РК 🇰🇿", callback_data='alm1')
                ast = types.InlineKeyboardButton("Нур-Султан, РК 🇰🇿", callback_data='ast1')
                local = types.InlineKeyboardButton("Отправить ГЕО 📍", callback_data='local')

                markup.add(ast)
                markup.add(alm)
                markup.add(shym)
                markup.add(moscow)
                markup.add(piter)
                markup.add(kazan)
                markup.add(ekb)
                markup.add(nov)
                markup.add(kalin)
                markup.add(local)

                bot.send_message(message.chat.id, 'Список городов:', reply_markup=markup)
            elif message.text == 'COVID-19🦠':
                cvd_panel(message)
                # bot.send_message(message.chat.id, 'На данный момент этот раздел закрыт!\nПриносим свои извинения.')

            elif message.text == 'Соц.Сети📱':
                bot.delete_message(message.chat.id, message.message_id)
                call_social(message)

            elif message.text == 'Оставить отзыв ⭐️':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("⭐️", callback_data='star1')
                item2 = types.InlineKeyboardButton("⭐️⭐️", callback_data='star2')
                item3 = types.InlineKeyboardButton("⭐️⭐️⭐️", callback_data='star3')
                item4 = types.InlineKeyboardButton("⭐️⭐️⭐️⭐️", callback_data='star4')
                item5 = types.InlineKeyboardButton("⭐️⭐️⭐️⭐️⭐️", callback_data='star5')

                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                markup.add(item5)

                bot.send_message(message.chat.id, 'Оцените наш телеграмм бот', reply_markup=markup)

            elif message.text == 'Инфо📋': # удалить через 30 дней (15.04.2020)
                next(message)
            elif message.text == '[Далее]':
                next(message)
            elif message.text == 'Версия БОТа 🤖':
                version(message)
            elif message.text == 'Создатели 👨🏻‍💻':
                creator(message)
            elif message.text == 'Обратная связь 📞':
                callback(message)
            elif message.text == '[Назад]':
                mainkeyboard(message)
            elif message.text == 'Игры 🎮':

                markup = types.InlineKeyboardMarkup(row_width=2)
                gms = types.InlineKeyboardButton(text='перейти', url='https://t.me/gamee', callback_data='gms')
                markup.add(gms)

                bot.send_message(message.chat.id, 'Вот ссылка на бота, где можно поиграть прямо в телеграмме', reply_markup=markup)
            elif message.text == 'Анекдот😂':
                answer = "Хочет почитать анекдота"
                txt(message, answer)
                bot.send_chat_action(message.chat.id, 'typing')
                bot.reply_to(message, getanekdot())
            elif message.text == 'Телеграмм бот от наших друзей':
                markup = types.InlineKeyboardMarkup(row_width=2)

                cg = types.InlineKeyboardButton(text='CINEMA GEEKS', url='t.me/CINEMAGEEKS_bot')
                tl = types.InlineKeyboardButton(text='Traffic laws helper', url='t.me/Trafficlawshelper_bot')

                markup.add(cg)
                markup.add(tl)

                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJJc16aMpxBTXMUFrsFJ0PLBgEE7wTUAAKIBQACztjoC231wM7ctbTjGAQ')
                bot.send_message(message.chat.id, 'Советую вам воспользоваться другими сервисами от наших друзей:', reply_markup=markup)
            ################################################################################################
            #                                         Пасхальное яйцо                                      #
            ################################################################################################
            elif message.text == 'frog' or message.text == 'Frog':
                answer = "Нашел(нашла) пасхалку!"
                txt(message, answer)
                file_id = 'CAACAgIAAxkBAAIx0l5qeu-IDGRasmaNpRkWBVqDDabQAAIFAAN1UIETZmBnin0s48QYBA'
                bot.send_sticker(message.chat.id, file_id)
                bot.send_message(message.chat.id, 'Молодец, ты нашел(нашла) пасхалку!')
            elif message.text == 'Cat' or message.text == 'cat':
                answer = "Нашел(нашла) пасхалку!"
                txt(message, answer)
                file_id = 'CCAACAgEAAxkBAAJJi16aNd-t3WsKg2mP5wclzXKpN7yGAAIDCgACv4yQBJGkR4JOgqlxGAQ'
                bot.send_sticker(message.chat.id, file_id)
                bot.send_message(message.chat.id, 'Молодец, ты нашел(нашла) пасхалку!')
            elif message.text == 'Dog' or message.text == 'dog':
                answer = "Нашел(нашла) пасхалку!"
                txt(message, answer)
                file_id = 'CAACAgIAAxkBAAJJiV6aNbsOQZ0NlZTXaRYZ0j_nYZqxAAIHAAOKfy43zv_oD7S3blYYBA'
                bot.send_sticker(message.chat.id, file_id)
                bot.send_message(message.chat.id, 'Молодец, ты нашел(нашла) пасхалку!')
            elif message.text == 'Freeman' or message.text == 'freeman':
                answer = "Нашел(нашла) пасхалку!"
                txt(message, answer)
                file_id = 'CAACAgQAAxkBAAIx1F5qe7vr5tUe-ROJwKTyaRwkSvemAAJRAAODatAQ9LqbS-wgwS8YBA'
                bot.send_sticker(message.chat.id, file_id)
                bot.send_message(message.chat.id, 'Я вам ничего не должен, это вы должны себе.')
            elif message.text == 'no rules' or message.text == 'No rules' or message.text == '/no_rules' or message.text == 'no rules!' or message.text == 'No rules!' or message.text == 'танцуем' or message.text == 'Танцуем' or message.text == 'dance' or message.text == 'Dance' or message.text == 'party hard' or message.text == 'Party hard':
                answer = "Нашел(нашла) пасхалку!"
                bot.send_chat_action(message.chat.id, 'find_location')
                txt(message, answer)
                audio = open('No Rules!.mp3', 'rb')
                bot.send_audio(message.chat.id, audio)
                file_id = 'CAACAgIAAxkBAAJJdV6aMsIIj21ygdN9Ssm9sTQJptcRAAKLBQACztjoC6GpRX_jrcCsGAQ'
                bot.send_sticker(message.chat.id, file_id)
                bot.send_message(message.chat.id, 'Го тусить!')
            ################################################################################################
            ###                                      Фильтр мата                                         ###
            ################################################################################################
            elif message.text == 'сука' or message.text == 'Сука' or message.text == 'пидор' or message.text == 'Пидор' or message.text == 'пидарас' or message.text == 'Пидарас' or message.text == 'пизда' or message.text == 'Пизда' or message.text == 'хуй' or message.text == 'Хуй' or message.text == 'Xyu' or message.text == 'xyu' or message.text == 'гондон' or message.text == 'Гондон' or message.text == 'блять' or message.text == 'Блять' or message.text == 'бля' or message.text == 'Бля' or message.text == 'хер' or message.text == 'Хер' or message.text == 'Херь' or message.text == 'херь' or message.text == 'лох' or message.text == 'Лошара' or message.text == 'залупа' or message.text == 'Залупа' or message.text == 'охуенно' or message.text == 'Охуенно' or message.text == 'мудак' or message.text == 'Мудак' or message.text == 'Мразь' or message.text == 'мразь' or message.text == 'пердун' or message.text == 'Пердун' or message.text == 'пиздеть' or message.text == 'анал' or message.text == 'Анал' or message.text == 'Пиздеть' or message.text == 'жопа' or message.text == 'Жопа' or message.text == 'падла' or message.text == 'Падла' or message.text == 'Похуй' or message.text == 'похуй' or message.text == 'нигга' or message.text == 'Нигга' or message.text == 'Нигер' or message.text == 'нигер' or message.text == 'Хуйня' or message.text == 'хуйня':
                bot.delete_message(message.chat.id, message.message_id)
                answer = "Обзывается!"
                txt(message, answer)
                file_id = 'CAACAgIAAxkBAAJJh16aNSzWrVcaD45W3Q-z_GHiV3tZAAJxBQACztjoCwR34r4skuTsGAQ'
                bot.send_sticker(message.chat.id, file_id)
            ################################################################################################
            ###                             Значение ELSE в текстовых сообщениях                         ###
            ################################################################################################
            else:
                answer = "ПИШЕТ ДИЧЬ"
                txt(message, answer)
                file_id = 'CAACAgIAAxkBAAJJd16aMxnK0_4SE4Swc17FUSL5e6wLAAKlBQACztjoC-kLCo3s8H9xGAQ'
                bot.send_sticker(message.chat.id, file_id)
                bot.send_message(message.chat.id, 'Я не знаю что ответить!')

################################################################################################################################################################################################
###                                                                                   CAllBAC InlineKeyboards                                                                                ###
################################################################################################################################################################################################
#InlineKeyboards
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            ################################################################################################
            ###                                CALLBACK Оставить отзыв                                   ###
            ################################################################################################
            if call.data == 'star1':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                callans = "1"
                star(call, callans)
                file_id = 'CAACAgIAAxkBAAJJeV6aMy1hWwz0Xh2mqJSqCVyZF9TxAAJ6BQACztjoC2HJ4Rcvib92GAQ'
                sti = bot.send_sticker(call.message.chat.id, file_id)
                bot.send_message(call.message.chat.id, 'Возможно, это не для Вас.')
            elif call.data == 'star2':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                callans = "2"
                star(call, callans)
                file_id = 'CAACAgIAAxkBAAJJe16aMznGD4e4CL0w4zBOY_XI4i2sAAJ8BQACztjoC_7XeYL8ab6XGAQ'
                sti = bot.send_sticker(call.message.chat.id, file_id)
                bot.send_message(call.message.chat.id, 'Мы работаем над ошибками.')

            elif call.data == 'star3':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                callans = "3"
                star(call, callans)
                file_id = 'CAACAgIAAxkBAAJJfV6aM06fBSwiFrxMwR9i3h5NZUT1AAKMBQACztjoC4V1-fyGKIxNGAQ'
                sti = bot.send_sticker(call.message.chat.id, file_id)
                bot.send_message(call.message.chat.id, 'Будем стараться!')

            elif call.data == 'star4':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                callans = "4"
                star(call, callans)
                file_id = 'CAACAgIAAxkBAAJJf16aM1u0lPf2abnujaJQrmy4AoOLAAKiBQACztjoC61sVQ-LShGEGAQ'
                sti = bot.send_sticker(call.message.chat.id, file_id)
                bot.send_message(call.message.chat.id, 'Спасибо. Заходите еще!')
            elif call.data == 'star5':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                callans = "5"
                star(call, callans)
                file_id = 'CAACAgIAAxkBAAJJgV6aM2dC8hez2d9BmE7U3cHD_q2QAAKBBQACztjoC8fgM5-5KThxGAQ'
                sti = bot.send_sticker(call.message.chat.id, file_id)
                bot.send_message(call.message.chat.id, 'И мы тебя любим!', sti)
            ################################################################################################
            ###                                  CALLBACK Погода                                         ###
            ################################################################################################
            elif call.data == 'moscow1':
                weather_city = "Moscow,RU"
                weather_city1 = "Москва"
                weather_city2 = "Москве"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'piter1':
                weather_city = "Saint Petersburg, RU"
                weather_city1 = "Санкт-Петербург"
                weather_city2 = "Питере"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'kazan1':
                weather_city = "Kazan', RU"
                weather_city1 = "Казань"
                weather_city2 = "Казани"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'ekb1':
                weather_city = "Ekaterinburg, RU"
                weather_city1 = "Екатеринбург"
                weather_city2 = "Екатеринбурге"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'nov1':
                weather_city = "Novosibirsk, RU"
                weather_city1 = "Новосибирск"
                weather_city2 = "Новосибирске"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'kalin1':
                weather_city = "Kaliningrad, RU"
                weather_city1 = "Калининград"
                weather_city2 = "Калининграде"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'shym1':
                weather_city = "Shymkent, KZ"
                weather_city1 = "Шымкент"
                weather_city2 = "Шымкенте"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'alm1':
                weather_city = "Almaty, KZ"
                weather_city1 = "Алматы"
                weather_city2 = "Алмате"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'ast1':
                weather_city = "Nur-Sultan,KZ"
                weather_city1 = "Нур-Султан"
                weather_city2 = "Нур-Султане"
                weather_owm(call, weather_city, weather_city1, weather_city2)
            elif call.data == 'local':
                global weather_local
                bot.delete_message(call.message.chat.id, call.message.message_id)
                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                button_geo = types.KeyboardButton(text="Отправить местоположение 📍", request_location=True)
                back = types.KeyboardButton(text="[Назад]")
                keyboard.add(button_geo)
                keyboard.add(back)
                weather_local = bot.send_message(call.message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение, для получения сведений о погоде.", reply_markup=keyboard)
            ################################################################################################
            ###                                     CALLBACK Соц. сети                                   ###
            ################################################################################################
            elif call.data == 'callback_func':
                markup = types.InlineKeyboardMarkup(row_width=2)

                video_in_audio_yt = types.InlineKeyboardButton("Конвертация аудио в видео из YouTube", callback_data='v_i_a_yt')
                dwnl_video_yt = types.InlineKeyboardButton("Скачать видео из YouTube", callback_data='d_v_yt')
                dwnl_photo_ins = types.InlineKeyboardButton("Скачать фото из Instagram", callback_data='d_p_ins')
                dwnl_video_ins = types.InlineKeyboardButton("Скачать видео из Instagram", callback_data='d_v_ins')

                markup.add(video_in_audio_yt)
                markup.add(dwnl_video_yt)
                markup.add(dwnl_photo_ins)
                markup.add(dwnl_video_ins)


                bot.send_message(call.message.chat.id, 'Список функционала:', reply_markup=markup)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'v_i_a_yt':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                ansfunc = ("Хочеть конвертировать видео в аудио из YouTube")
                func(call, ansfunc)

                markup = types.InlineKeyboardMarkup(row_width=2)

                ins = types.InlineKeyboardButton(text='перейти', url='t.me/foresti2_bot')
                back_func = types.InlineKeyboardButton(text='назад', callback_data= 'callback_func' )

                markup.add(ins)
                markup.add(back_func)

                bot.send_message(call.message.chat.id, '\n*Инструкция*:\
                                                    \n1. Нажмите на кнопку "перейти"\
                                                    \n2. /start (Если вы впервые запускаете)\
                                                    \n3. Вставляете ссылку на видео\
                                                    \n4. Ждите несколько минут', parse_mode='markdown', reply_markup=markup)


            elif call.data == 'd_v_yt':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                ansfunc = ("Хочеть скачать видео из YouTube")
                func(call, ansfunc)
                markup = types.InlineKeyboardMarkup(row_width=2)

                ins = types.InlineKeyboardButton(text='перейти', url='t.me/foresti3_bot')
                back_func = types.InlineKeyboardButton(text='назад', callback_data= 'callback_func' )

                markup.add(ins)
                markup.add(back_func)

                bot.send_message(call.message.chat.id, '\n*Инструкция*:\
                                                    \n1. Нажмите на кнопку "перейти"\
                                                    \n2. /start (Если вы впервые запускаете)\
                                                    \n3. Вставляете ссылку на видео\
                                                    \n4. Выберите разрешение видео\
                                                    \n4. Ждите несколько секунд', parse_mode='markdown', reply_markup=markup)

            elif call.data == 'd_p_ins':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                ansfunc = ("Хочеть скачать фото из Instagram")
                func(call, ansfunc)
                markup = types.InlineKeyboardMarkup(row_width=2)

                ins = types.InlineKeyboardButton(text='перейти', url='t.me/foresti3_bot')
                back_func = types.InlineKeyboardButton(text='назад', callback_data= 'callback_func' )

                markup.add(ins)
                markup.add(back_func)

                bot.send_message(call.message.chat.id, '\n*Инструкция*:\
                                                    \n1. Нажмите на кнопку "перейти"\
                                                    \n2. /start (Если вы впервые запускаете)\
                                                    \n3. Вставляете ссылку на пост\
                                                    \n4. Ждите несколько секунд', parse_mode='markdown', reply_markup=markup)

            elif call.data == 'd_v_ins':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                ansfunc = ("Хочеть скачать видео из Instagram")
                func(call, ansfunc)
                markup = types.InlineKeyboardMarkup(row_width=2)

                ins = types.InlineKeyboardButton(text='перейти', url='t.me/foresti3_bot')
                back_func = types.InlineKeyboardButton(text='назад', callback_data= 'callback_func' )

                markup.add(ins)
                markup.add(back_func)

                bot.send_message(call.message.chat.id, '\n*Инструкция*:\
                                                    \n1. Нажмите на кнопку "перейти"\
                                                    \n2. /start (Если вы впервые запускаете)\
                                                    \n3. Вставляете ссылку на пост\
                                                    \n4. Ждите несколько секунд', parse_mode='markdown', reply_markup=markup)
            ################################################################################################
            ###                                      CALL BACK COVID-19 Страны                           ###
            ################################################################################################
            elif call.data == 'ru_cvd':
                location = covid19.getLocationByCountryCode("RU")
                mess = f"""В *России* 🇷🇺 \nНаселение: *{location[0]['country_population']}* \nЗаражений за всё время: *{location[0]['latest']['confirmed']}* \nСмертей: *{location[0]['latest']['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJG8F6V1CPNwH5Aywe4AAG-xgEosWAWuAAC5wEAAladvQoNeVnL-khcCxgE')
                bot.delete_message(call.message.chat.id, cvd_sticker.message_id)
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'kz_cvd':
                location = covid19.getLocationByCountryCode("KZ")
                mess = f"""В *Казахстане* 🇰🇿 \nНаселение: *{location[0]['country_population']}* \nЗаражений за всё время: *{location[0]['latest']['confirmed']}* \nСмертей: *{location[0]['latest']['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJG8F6V1CPNwH5Aywe4AAG-xgEosWAWuAAC5wEAAladvQoNeVnL-khcCxgE')
                bot.delete_message(call.message.chat.id, cvd_sticker.message_id)
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)

            elif call.data == 'bl_cvd':
                location = covid19.getLocationByCountryCode("BY")
                mess = f"""В *Белоруссии 🇧🇾* \nНаселение: *{location[0]['country_population']}* \nЗаражений за всё время: *{location[0]['latest']['confirmed']}* \nСмертей: *{location[0]['latest']['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJG8F6V1CPNwH5Aywe4AAG-xgEosWAWuAAC5wEAAladvQoNeVnL-khcCxgE')
                bot.delete_message(call.message.chat.id, cvd_sticker.message_id)
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'uk_cvd':
                location = covid19.getLocationByCountryCode("UA")
                mess = f"""В *Украине* 🇺🇦 \nНаселение: *{location[0]['country_population']}* \nЗаражений за всё время: *{location[0]['latest']['confirmed']}* \nСмертей: *{location[0]['latest']['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJG8F6V1CPNwH5Aywe4AAG-xgEosWAWuAAC5wEAAladvQoNeVnL-khcCxgE')
                bot.delete_message(call.message.chat.id, cvd_sticker.message_id)
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'uz_cvd':
                location = covid19.getLocationByCountryCode("UZ")
                mess = f"""В *Узбекистане 🇺🇿* \nНаселение: *{location[0]['country_population']}* \nЗаражений за всё время: *{location[0]['latest']['confirmed']}* \nСмертей: *{location[0]['latest']['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'it_cvd':
                location = covid19.getLocationByCountryCode("IT")
                mess = f"""В *Италии 🇮🇹* \nНаселение: *{location[0]['country_population']}* \nЗаражений за всё время: *{location[0]['latest']['confirmed']}* \nСмертей: *{location[0]['latest']['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJG8F6V1CPNwH5Aywe4AAG-xgEosWAWuAAC5wEAAladvQoNeVnL-khcCxgE')
                bot.delete_message(call.message.chat.id, cvd_sticker.message_id)
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'us_cvd':
                location = covid19.getLocationByCountryCode("US")
                mess = f"""В *США 🇺🇸* \nНаселение: *{location[0]['country_population']}* \nЗаражений за всё время: *{location[0]['latest']['confirmed']}* \nСмертей: *{location[0]['latest']['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJG8F6V1CPNwH5Aywe4AAG-xgEosWAWuAAC5wEAAladvQoNeVnL-khcCxgE')
                bot.delete_message(call.message.chat.id, cvd_sticker.message_id)
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'pl_cvd':
                location = covid19.getLocationByCountryCode("PL")
                mess = f"""В *Польше 🇵🇱* \nНаселение: *{location[0]['country_population']}* \nЗаражений за всё время: *{location[0]['latest']['confirmed']}* \nСмертей: *{location[0]['latest']['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJG8F6V1CPNwH5Aywe4AAG-xgEosWAWuAAC5wEAAladvQoNeVnL-khcCxgE')
                bot.delete_message(call.message.chat.id, cvd_sticker.message_id)
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'world_cvd':
                location = covid19.getLatest()
                mess = f"""В *Мире 🌏* \nЗаражений за всё время: *{location['confirmed']}* \nСмертей: *{location['deaths']}* \n[Подробнее...](https://yandex.ru/maps/covid19) \n\n[Рекомендации от ВОЗ](https://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019/advice-for-public)"""
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJG8F6V1CPNwH5Aywe4AAG-xgEosWAWuAAC5wEAAladvQoNeVnL-khcCxgE')
                bot.delete_message(call.message.chat.id, cvd_sticker.message_id)
                bot.send_message(call.message.chat.id, mess, parse_mode='markdown', disable_web_page_preview=True)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            ################################################################################################
            # Уведомление
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #     text="спасибо за отзыв!")
    except Exception as e:
        print(repr(e))
################################################################################################
###                     Принимает локацию от пользователя/погода                             ###
################################################################################################
@bot.message_handler(content_types=["location"])
def location(message):
        owm = pyowm.OWM('945a394890eab9e4e54bdda87d5e37e7', language="ru")
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, weather_local.message_id)
        obs = owm.weather_at_coords(message.location.latitude, message.location.longitude)
        w = obs.get_weather()  # поулчаем всю погоду из этого города

        temp = w.get_temperature('celsius') ["temp"]
        speed = w.get_wind() ["speed"]
        tempmin = w.get_temperature('celsius') ["temp_min"]
        tempmax = w.get_temperature('celsius') ["temp_max"]

        if temp < -20:
            answer_weather = "\n\n[Лучше сидеть дома!]"
        elif temp < -10:
            answer_weather = "\n\n[На улице мороз, возми перчатки!]"
        elif temp < 0:
            answer_weather = "\n\n[На улице очень холодно! Не забудь шапку!]"
        elif temp < 15:
            answer_weather = "\n\n[Сейчас холодно, одевайся потеплее.]"
        elif temp < 35:
            answer_weather = "\n\n[Температура норм, надевай что угодно.]"
        else:
            answer_weather = "\n\n[На улице жара]"
            file_id = 'CAACAgIAAxkBAAI_5V6NxC18AVgHWhOUDJeVPl1wiOJvAAICAwACusCVBTRFBuRNlNodGAQ'
            bot.send_sticker(message.chat.id, file_id)

        key = types.ReplyKeyboardMarkup(resize_keyboard=True)

        next = types.KeyboardButton("[Далее]")
        social = types.KeyboardButton("Соц.Сети📱")
        games = types.KeyboardButton("Игры 🎮")
        weather = types.KeyboardButton("Погода ⛅️")
        anekdot = types.KeyboardButton("Анекдот😂")
        virus = types.KeyboardButton("COVID-19🦠")

        key.row(social)
        key.row(games, anekdot)
        key.row(weather, virus)
        key.row(next)


        bot.send_message(message.chat.id,"В твоем городе, сейчас: " + w.get_detailed_status() + "\nТекущая температура составляет: " + str(temp)+ " °C." + "\nMin/Max = " + str(tempmin) + " / " + str(tempmax) + " °C" + " \nСкорость ветра составляет: " + str(speed) + " м/с" + str(answer_weather), reply_markup=key)
################################################################################################################################################################################################
####                                                                                         Антифлуд                                                                                       ####
################################################################################################################################################################################################
@bot.message_handler(content_types=['sticker', 'audio', 'vidio', 'vidio_note', 'voice', 'photo', 'document', 'emoji'])
def sticker_handler(message):
    bot.delete_message(message.chat.id, message.message_id)
################################################################################################################################################################################################
#Терминал запуска
print('------------ Foresti Team -------------')
print('Тип Бота - Главный')
print('Название Телегармм Бота - "Foresti Bot"')
print('Запуск кода...')
print('код успешно запущен!')
print('---------------------------------------')
#Сообщение админу
bot.send_message(admin_id, '`СЕРВЕР:` _Бот_ _успешно_ _запущен!_', parse_mode='markdown')
################################################################################################################################################################################################
#Запуск бота
bot.polling(none_stop=True)
################################################################################################################################################################################################
####                                                                                      Foresti 2020                                                                                      ####
################################################################################################################################################################################################
