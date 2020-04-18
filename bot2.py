################################################################################################
####                                    Foresti 2020                                        ####
################################################################################################
import telebot
import youtube_dl
from telebot import types
import os
import time
from configbot import TOKEN2
from configbot import admin_id
################################################################################################
#Токен
bot = telebot.TeleBot(TOKEN2)
ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
################################################################################################
def txt(message, answer):
    print("\n---------Foresti_CMD---------")
    print(time.ctime(int(time.time())), "\nUSER: @{0}\
                                         \nИмя: {1}\
                                         \nФамилия: {2}\
                                         \nID: {3}\n\
                                         \nСсылка на видео: {4}".format(message.from_user.username,
                                                                  message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print("->", answer, "<-")
    print("-----------------------------")
################################################################################################

################################################################################################
@bot.message_handler(commands=['start'])
def command_start(message):
    print("\n---------Foresti_CMD---------")
    print(time.ctime(int(time.time())), "\nUSER: @{0}\
                                         \nИмя: {1}\
                                         \nФамилия: {2}\
                                         \nID: {3}\n".format(message.from_user.username,
                                                                  message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id)))
    print("Запустил бота!")
    print("-----------------------------")
    # file_id = 'CAACAgIAAxkBAAI0I15ycJiAvosaMEgRZecAAVWBYXZpmAACGwADh_91F7iAyCpRqOOIGAQ'
    # bot.send_sticker(message.chat.id, file_id)

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # help = types.KeyboardButton("HELP")
    # markup.add(help)

    markup = types.InlineKeyboardMarkup(row_width=2)
    back = types.InlineKeyboardButton(text='назад', url='https://t.me/foresti_bot')
    markup.add(back)
    bot.send_message(message.chat.id, "*Вы* только что перешли на другого бота который выполняет ограниченную функцию\
                                            \nЧтобы узнать и использовать функционал бота нажмите на кнопку [*/help*’]\
                                            \nЕсли выхоите вернуться нажмите на кнопку *назад*.".format(message.from_user, bot.get_me()), parse_mode='markdown', reply_markup=markup)
    pass
################################################################################################
@bot.message_handler(commands=['version'])
def command_version(message):
    bot.send_message(message.chat.id, 'Версия `1.5.1-b`', parse_mode='markdown')
    pass
################################################################################################
@bot.message_handler(commands=['help'])
def command_help(message):
    # photo = open('home/nurmukhammed/helpyt.jpg', 'rb')
    # bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Просто пришлите мне ссылку на видео из YouTube.\nПример(https://www.youtube.com/watch?v=***********)')".format(message.from_user, bot.get_me()), parse_mode='html')
    pass
################################################################################################

################################################################################################
@bot.message_handler(regexp='youtube.com/\D|youtu.be/')
def download_video(message):
    try:
        answer = "КОНВЕРТАЦИЯ..."
        txt(message, answer)
        global d_file
        global message_send
        global file_caption
        global info
        message_send = bot.send_message(message.chat.id, "Обраватываю запрос ...")
        if 'youtube.com' in message.text or 'youtu.be' in message.text:
            with youtube_dl.YoutubeDL() as ydl:
                d_file = message.text
                bot.delete_message(message.chat.id, message.message_id)
                message_send = bot.edit_message_text(text="Парсим запрос ...", chat_id=message.chat.id, message_id=message_send.message_id)
                info = ydl.extract_info(message.text, download=False)
                file_caption = f"<b>Названия файла:</b> {info['title']} \n<b>Число просмотров:</b> {info['view_count']} \n<b>Число лайков:</b> {info['like_count']} \n<b>Число дизлайков:</b> {info['dislike_count']}"
                # Здесь конфигурация Инлайн-клавиатуры
                start_keyboard = types.InlineKeyboardMarkup()
                b_audio = types.InlineKeyboardButton(text='Скачать аудио', callback_data='audio')
                start_keyboard.add(b_audio)
                bot.delete_message(message.chat.id, message_send.message_id)
                # Отправлется обложка фотографии вместе с клавиатурой
                message_send = bot.send_photo(message.chat.id, info["thumbnail"], file_caption, parse_mode="HTML", reply_markup=start_keyboard)
    except:
        bot.delete_message(message.chat.id, message_send.message_id)
        bot.send_message(message.chat.id, 'Ссылка не действительно!')
################################################################################################

################################################################################################
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'audio':
        try:

            bot.delete_message(call.message.chat.id, call.message.message_id)
            sticker = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAI05l5z-TBMv-dNKcGS0BKHBMjH393WAAItAAOcL18Hb_ByKvuRBV8YBA')
            message_send = bot.send_message(call.message.chat.id, "Загрузка...")
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # os.listdir('music')
                ydl.download([d_file])
                filename = ydl.extract_info(d_file)['title']+"-"+ydl.extract_info(d_file)['id']
                for file in os.listdir():
                    if file.split(".")[0] == filename:
                        f = open(file, 'rb')
                        bot.delete_message(call.message.chat.id, sticker.message_id)
                        bot.delete_message(call.message.chat.id, message_send.message_id)
                        bot.send_audio(call.message.chat.id, f, info['title'], parse_mode="HTML")
                        pass
        except:
            bot.delete_message(call.message.chat.id, sticker.message_id)
            bot.delete_message(call.message.chat.id, message_send.message_id)
            bot.send_message(call.message.chat.id, 'Ошибка!')
################################################################################################

################################################################################################
@bot.message_handler(content_types=['text', 'sticker', 'audio', 'vidio', 'vidio_note', 'voice', 'photo', 'document', 'emoji'])
def text(message):
    bot.delete_message(message.chat.id, message.message_id)
    pass
################################################################################################
print('--------------- Foresti Team ----------------')
print('Тип Бота - Функциональный ')
print('Название Телегармм Бота - "Foresti YT Music"')
print('Запуск кода...')
print('код успешно запущен!')
print('---------------------------------------------')
#Сообщение админу
bot.send_message(admin_id, '`СЕРВЕР:` _Бот_ _успешно_ _запущен!_', parse_mode='markdown')
################################################################################################
bot.polling(none_stop=True, timeout=20)
################################################################################################
####                                    Foresti 2020                                        ####
################################################################################################
