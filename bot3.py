################################################################################################
####                                    Foresti 2020                                        ####
################################################################################################
import os
import time
from shutil import rmtree
from configbot import TOKEN3

from telegram import InputMediaPhoto, InputMediaVideo, InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    CallbackQueryHandler

from utils import get_insta_links, check_instagram, check_youtube, \
    get_youtube_resolutions, download_yt_video, get_yt_link_by_res
###############################################################################################

###############################################################################################
def main():
    updater = Updater(TOKEN3, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("version", version))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()
###############################################################################################

###############################################################################################
def start(update, context):
    update.message.reply_text('*Вы* только что перешли на другого бота который выполняет ограниченную функцию\
                                            \nЧтобы узнать и использовать функционал бота нажмите на кнопку [*/help*’]\
                                            \nЕсли выхоите вернуться нажмите на кнопку *назад*.', reply_markup = InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(text="назад", url="t.me/foresti_bot")]]), parse_mode='markdown')

def help(update, context):
    update.message.reply_text(
        'Просто пришлите мне ссылку на пост из Instagram.\
        \nили же ссылку на видео из YouTube\
        \nПример:\
        \n(https://www.instagram.com/p/*****************)\
        \n(https://www.youtube.com/watch?v=*************)')

def version(update, context):
    update.message.reply_text(
        'Версия 0.7.9-b')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def button(update, context):
    query = update.callback_query

    context.bot.deleteMessage(query.from_user.id, query.message.message_id)

    social_network, video_id, res, size = query.data.split('--')

    if float(size) > 50:
        if social_network == 'yt':
            url = get_yt_link_by_res(video_id, res)
        context.bot.send_message(chat_id=query.from_user.id,
                                 parse_mode='Markdown',
                                 text="Telegram позволяет отправлять видео только до 50 мб, поэтому мы можем дать только прямую [ссылку](" + url + ")")
    else:
        context.bot.send_message(query.from_user.id,
                                 "Ваше видео загружается ...")
        if 'yt' in social_network:
            flag, path = download_yt_video(video_id, res)

        video_file = open(path, 'rb')
        context.bot.send_video(update.callback_query.from_user.id, video_file,
                               timeout=200)

        rmtree(os.path.join("files", path.split('/')[1]), ignore_errors=True)
###############################################################################################

###############################################################################################
def handle_message(update, context):
    result = 0
    reason = ''

    if update.message:

        url = update.message.text

        if check_instagram(url):
            flag, post = get_insta_links(url)

            contents = []

            try:
                for node in post.get_sidecar_nodes():
                    contents.append(node)

                if flag:

                    media_group = []
                    context.bot.send_message(update.message.chat.id,
                                             "Ваши данные загружаются ...")

                    if len(contents):
                        for node in contents:
                            if node.is_video:
                                # print(node.video_url)
                                media_group.append(
                                    InputMediaVideo(node.video_url))
                            else:
                                media_group.append(
                                    InputMediaPhoto(node.display_url))
                        context.bot.sendMediaGroup(update.message.chat.id,
                                                   media_group, timeout=200)
                    else:
                        if post.is_video:

                            context.bot.sendMediaGroup(update.message.chat.id, [
                                InputMediaVideo(post.video_url)],
                                                       timeout=200)
                        else:
                            context.bot.sendMediaGroup(update.message.chat.id, [
                                InputMediaPhoto(post.url)], timeout=200)

                    if post.caption:
                        context.bot.send_message(update.message.chat.id,
                                                 post.caption)

                    result = 1
                else:
                    reason = 'Instagram error'
                    context.bot.sendMessage(update.message.chat.id,
                                            "Неверная ссылка. Проверьте, является ли видео публичным.")
            except Exception as e:
                print(str(e))
                context.bot.sendMessage(update.message.chat.id,
                                        "Неверная ссылка. Проверьте, является ли видео публичным.")

        elif check_youtube(url):
            flag, streams, video_id = get_youtube_resolutions(url)

            if flag:

                keyboard = []

                for stream in streams:
                    text = stream.res.split('.')[0] + ' (' + str(
                        stream.size) + 'МБ)'
                    callback_data = "yt" + "--" + video_id + '--' + stream.res + '--' + str(
                        stream.size)
                    keyboard.append([InlineKeyboardButton(text=text,
                                                          callback_data=callback_data)])

                reply_markup = InlineKeyboardMarkup(keyboard)

                context.bot.send_message(update.message.chat.id,
                                         text="Выберите разрешение",
                                         reply_markup=reply_markup)
                result = 1
            else:
                context.bot.sendMessage(update.message.chat.id,
                                        "Неверная ссылка.")
                reason = 'Youtube error'

        else:
            context.bot.sendMessage(update.message.chat.id,
                                    "Неверная ссылка!")
            reason = 'Неверная ссылка'

        print(update.message.from_user.name, update.message.text,
              time.ctime(int(time.time())), result, reason,
              sep='    ', flush=True)

        user_exist = db_users.search(
            query.user == update.message.from_user.name)

        if len(user_exist) == 0:
            db_users.insert({'user': update.message.from_user.name,
                             'chat_id': update.message.chat.id})

###############################################################################################
print('--------------- Foresti Team ----------------')
print('Тип Бота - Функциональный ')
print('Название Телегармм Бота - "Foresti BOT 3"')
print('Запуск кода...')
print('код успешно запущен!')
print('---------------------------------------------')
###############################################################################################
if __name__ == '__main__':
    main()
################################################################################################
####                                    Foresti 2020                                        ####
################################################################################################
