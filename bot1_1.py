import telebot
import os
import random
import urllib.request as urllib2

token="554192076:AAG_LTd1yE2rrDle0Z_JRvHAKLVZPvoVKGs"
bot=telebot.TeleBot(token)

#bot.send_message(258340140,"testik")

#upd=bot.get_updates()

#last_upd=upd[-1]
#message_from_user=last_upd.message

#print(message_from_user)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'фото':
        url = 'https://www.youtube.com/yts/img/yt_1200-vfl4C3T0K.png'
        urllib2.urlretrieve(url,"url_image")
        #all_files_of_directory=os.listdir(directory)
       # random_file=random.choice(all_files_of_directory)
        img=open('url_image','rb')
        bot.send_chat_action(message.from_user.id,'upload_photo')
        bot.send_photo(message.from_user.id,img)
        img.close()

    elif message.text == 'аудио':
        audio = open('C:/Users/User/PycharmProjects/imge/61078708_160562257.mp3', 'rb')
        bot.send_chat_action(message.from_user.id,'upload_audio')
        bot.send_audio(message.from_user.id,audio)
        audio.close()
    elif message.text == 'а':
        
        bot.send_message(message.from_user.id,"b")

bot.polling(none_stop=True,interval=0)