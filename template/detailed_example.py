# -*- coding: utf-8 -*-
"""
This is a detailed example using almost every command of the API
"""
import sys
sys.path.append('../')
import api
from settings import *
import time
import telebot
from telebot import types
from redis import Redis
reload(sys)
sys.setdefaultencoding("utf-8")
r = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

TOKEN = '834857847:AAH-_g84YhfoYW5Oc60KMtsaym8ByokJ0VA_AAAA'

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'       : 'Get used to the bot',
    'study'        : 'Study by topics',
    'memo'        : 'Learn forgetful words',
    'test'       : 'quit test',
    'help'        : 'Gives you information about the available commands',
    'sendLongText': 'A test using the \'send_chat_action\' command',
    'getImage'    : 'A test using multi-stage messages, custom keyboard, and media sending'
}

commands_topic = api.get_commands_topic()

# imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # create the image selection keyboard
# imageSelect.add('cock', 'pussy','mv','cd')
imageSelect = types.ReplyKeyboardMarkup()
imageSelect.add("A")
imageSelect.add("B")
imageSelect.add("C")
imageSelect.add("D")

hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard

command = ['start']
command_topics = api.get_topics()
list_quetions_by_topic = []
globals()['list_quetions_by_topic'] = []
len_list = 0

# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
mv = "\t Feedback \n A : Phản hồi \n B : Người đại diện \n C : Nhàm chán \n D : Vcl"
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0

# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener
def check_anwer(text, memo = None):
    global index
    global list_quetions_by_topic
    if not memo:
        quet = list_quetions_by_topic[index]
    else:
        global index_memo
        global list_quetions_memo
        quet = list_quetions_memo[index_memo]

    if text == "A":
        if(quet.getAnsA() == quet.getAnswer()):
            return True,quet.getAnswer()
        else:
            return False,quet.getAnswer(),quet.getquestion()
    elif text == "B":
        if (quet.getAnsB() == quet.getAnswer()):
            return True,quet.getAnswer()
        else:
            return False,quet.getAnswer(),quet.getquestion()
    elif text == "C":
        if (quet.getAnsC() == quet.getAnswer()):
            return True,quet.getAnswer()
        else:
            return False,quet.getAnswer(),quet.getquestion()
    elif text == "D":
        if (quet.getAnsD() == quet.getAnswer()):
            return True,quet.getAnswer()
        else:
            return False,quet.getAnswer(),quet.getquestion()
    else:
        return False,quet.getAnswer(),quet.getquestion()
# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hello, stranger, let MinhVu scan you...")
        bot.send_message(cid, "Scanning complete, I know you now")
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "I already know you, no need for me to scan you again!")
# command start
@bot.message_handler(commands=['study'])
def study_by_topic(m):
    cid = m.chat.id
    help_text = "Please chose topic: \n"
    for key in commands_topic:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": \n"
        # help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)
@bot.message_handler(commands=command_topics)
def study_by_topic(m):
    cid = m.chat.id
    userStep[cid] = 3
    global list_quetions_by_topic
    list_quetions_by_topic = api.get_question_by_topic(m.text.replace('/',''))
    global index
    index = 0
    quet = list_quetions_by_topic[index]
    global len_list
    len_list = len(list_quetions_by_topic)
    global dem
    dem = 0
    mv1 = "----  {}  ---- \n A : {} \n B : {} \n C : {} \n D : {} \n ------ {}/{} ------ \n ".format(
                                                                quet.getquestion().encode('utf-8').strip(),
                                                                quet.getAnsA().encode('utf-8').strip(),
                                                                quet.getAnsB().encode('utf-8').strip(),
                                                                 quet.getAnsC().encode('utf-8').strip(),
                                                                  quet.getAnsD().encode('utf-8').strip(), index + 1,len_list)
    bot.send_message(cid, mv1)
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 3)
def show_quetions(m):
    cid = m.chat.id
    text = m.text

    # for some reason the 'upload_photo' status isn't quite working (doesn't show at all)
    # bot.send_chat_action(cid, 'typing')

    global index
    global len_list
    global dem
    if(index + 1 < len_list):

        if text == "A":
            print check_anwer('A')
            if check_anwer('A')[0] == False:
                bot.send_message(cid, "False . " + check_anwer('A')[1])
                api.set_forgetful_word(check_anwer('A')[2],check_anwer('A')[1],604800)
            else:
                dem += 1
        elif text == "B":
            if check_anwer('B')[0] == False:
                bot.send_message(cid, "False . " + check_anwer('A')[1])
                api.set_forgetful_word(check_anwer('A')[2], check_anwer('A')[1], 604800)
            else:
                dem += 1
        elif text == "C":
            if check_anwer('C')[0] == False:
                bot.send_message(cid, "False . " + check_anwer('A')[1])
                api.set_forgetful_word(check_anwer('A')[2], check_anwer('A')[1], 604800)
            else:
                dem += 1
        elif text == "D":
            if check_anwer('D')[0] == False:
                bot.send_message(cid, "False . " + check_anwer('A')[1])
                api.set_forgetful_word(check_anwer('A')[2], check_anwer('A')[1], 604800)
            else:
                dem += 1
        else:
            bot.send_message(cid, "Please try again")
            userStep[cid] = 0
        index += 1
        quet = list_quetions_by_topic[index]
        mv1 = "----  {}  ---- \n A : {} \n B : {} \n C : {} \n D : {} \n ------ {}/{} ------ \n ".format(
            quet.getquestion().encode('utf-8').strip(),
            quet.getAnsA().encode('utf-8').strip(),
            quet.getAnsB().encode('utf-8').strip(),
            quet.getAnsC().encode('utf-8').strip(),
            quet.getAnsD().encode('utf-8').strip(),index + 1,len_list)
        bot.send_message(cid, mv1, reply_markup=imageSelect)
    else:
        k1 = (dem_memo / len_list_memo) * 100
        if k1 > 50 and k1 < 75:
            mess = "Bad"
        elif k1 > 75 and k1 < 90:
            mess = "Pretty good"
        elif k1 > 90:
            mess = "Good"
        else:
            mess = "Fuck"
        bot.send_message(cid, "The result : {}/{}, {}!".format(dem,len_list,mess))
        dem = 0
        userStep[cid] = 0




# -------------------------------------------------end block /stydy ----------------------------------------------------





@bot.message_handler(commands=['memo'])
def study_memo(m):
    cid = m.chat.id
    bot.send_message(cid, "Please wait")
    userStep[cid] = 4
    global list_quetions_memo
    list_quetions_memo = api.get_words_forget()
    global index_memo
    index_memo = 0
    quet = list_quetions_memo[index_memo]
    global len_list_memo
    len_list_memo = len(list_quetions_memo)
    global dem_memo
    dem_memo = 0
    mv1 = "----  {}  ---- \n A : {} \n B : {} \n C : {} \n D : {} \n ------ {}/{} ------ \n ".format(
        quet.getquestion().encode('utf-8').strip(),
        quet.getAnsA().encode('utf-8').strip(),
        quet.getAnsB().encode('utf-8').strip(),
        quet.getAnsC().encode('utf-8').strip(),
        quet.getAnsD().encode('utf-8').strip(), index_memo + 1, len_list_memo)
    bot.send_message(cid, mv1)
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 4)
def show_quetions_memo(m):
    cid = m.chat.id
    text = m.text
    global index_memo
    global len_list_memo
    global dem_memo
    if(index_memo + 1 < len_list_memo):

        if text == "A":
            if check_anwer('A','minhvu')[0] == False:
                bot.send_message(cid, "False . " + check_anwer('A','minhvu')[1])
                api.set_forgetful_word(check_anwer('A','minhvu')[2],check_anwer('A','minhvu')[1],604800)
            else:
                dem_memo += 1
        elif text == "B":
            if check_anwer('B','minhvu')[0] == False:
                bot.send_message(cid, "False . " + check_anwer('A','minhvu')[1])
                api.set_forgetful_word(check_anwer('A','minhvu')[2], check_anwer('A','minhvu')[1], 604800)
            else:
                dem_memo += 1
        elif text == "C":
            if check_anwer('C','minhvu')[0] == False:
                bot.send_message(cid, "False . " + check_anwer('A','minhvu')[1])
                api.set_forgetful_word(check_anwer('A','minhvu')[2], check_anwer('A','minhvu')[1], 604800)
            else:
                dem_memo += 1
        elif text == "D":
            if check_anwer('D','minhvu')[0] == False:
                bot.send_message(cid, "False . " + check_anwer('A','minhvu')[1])
                api.set_forgetful_word(check_anwer('A','minhvu')[2], check_anwer('A','minhvu')[1], 604800)
            else:
                dem_memo += 1
        else:
            bot.send_message(cid, "Please try again")
            userStep[cid] = 0
        index_memo += 1
        quet = list_quetions_memo[index_memo]
        mv1 = "----  {}  ---- \n A : {} \n B : {} \n C : {} \n D : {} \n ------ {}/{} ------ \n ".format(
            quet.getquestion().encode('utf-8').strip(),
            quet.getAnsA().encode('utf-8').strip(),
            quet.getAnsB().encode('utf-8').strip(),
            quet.getAnsC().encode('utf-8').strip(),
            quet.getAnsD().encode('utf-8').strip(),index_memo + 1,len_list_memo)
        bot.send_message(cid, mv1, reply_markup=imageSelect)
    else:
        k1 = (dem_memo / len_list_memo) * 100
        if k1 > 50 and k1 < 75:
            mess = "Bad"
        elif k1 > 75 and k1 < 90:
            mess = "Pretty good"
        elif k1 > 90:
            mess = "Good"
        else:
            mess = "Fuck"
        bot.send_message(cid, "The result : {}/{}, {}!".format(dem_memo,len_list_memo,mess))
        dem_memo = 0
        userStep[cid] = 0


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page


# chat_action example (not a good one...)
@bot.message_handler(commands=['sendLongText'])
def command_long_text(m):
    cid = m.chat.id
    bot.send_message(cid, "If you think so...")
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(3)
    bot.send_message(cid, ".")


# user can chose an image (multi-stage command example)
@bot.message_handler(commands=['getImage'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Please choose your image now", reply_markup=imageSelect)  # show the keyboard
    # bot.send_message(cid, mv, reply_markup=imageSelect)  # show the keyboard
    userStep[cid] = 1  # set the user to the next step (expecting a reply in the listener now)


# if the user has issued the "/getImage" command, process the answer
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text

    # for some reason the 'upload_photo' status isn't quite working (doesn't show at all)
    bot.send_chat_action(cid, 'typing')

    if text == "cock":  # send the appropriate image based on the reply to the "/getImage" command
        bot.send_photo(cid, open('https://image2.tin247.com/pictures/2016/07/04/aqm1467622602.jpg', 'rb'),
                       reply_markup=hideBoard)  # send file and hide keyboard, after image is sent
        userStep[cid] = 0  # reset the users step back to 0
    elif text == "pussy":
        bot.send_photo(cid, open('kitten.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    else:
        bot.send_message(cid, "Don't type bullsh*t, if I give you a predefined keyboard!")
        bot.send_message(cid, "Please try again")
@bot.message_handler(commands=['test'])
def command_quiztest(m):
    cid = m.chat.id
    # bot.send_message(cid, "Please choose your image now", reply_markup=imageSelect)  # show the keyboard
    bot.send_message(cid, mv, reply_markup=imageSelect)  # show the keyboard
    userStep[cid] = 2
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 2)
def msg_answer_select(m):
    cid = m.chat.id
    text = m.text

    # for some reason the 'upload_photo' status isn't quite working (doesn't show at all)
    bot.send_chat_action(cid, 'typing')

    if text == "A":  # send the appropriate image based on the reply to the "/getImage" command
        bot.send_message(cid, "Chuẩn con mẹ nó rồi")  # send file and hide keyboard, after image is sent
        bot.send_message(cid, mv, reply_markup=imageSelect)
        userStep[cid] = 0  # reset the users step back to 0
    elif text == "B":
        bot.send_message(cid, "Don't type bullsh*t, if I give you a predefined keyboard!")
        userStep[cid] = 0
    elif text == "C":
        bot.send_message(cid, "Don't type bullsh*t, if I give you a predefined keyboard!")
        userStep[cid] = 0
    elif text == "D":
        bot.send_message(cid, "Don't type bullsh*t, if I give you a predefined keyboard!")
        userStep[cid] = 0
    else:
        bot.send_message(cid, "Don't type bullsh*t, if I give you a predefined keyboard!")
        bot.send_message(cid, "Please try again")
# filter on a specific message
@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you too!")


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "https://image2.tin247.com/pictures/2016/07/04/aqm1467622602.jpg")


bot.polling(none_stop=False, interval=0, timeout=20)
