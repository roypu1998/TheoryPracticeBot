from telebot import TeleBot
from telebot.types import ReplyKeyboardRemove
from db_TheoryQuestion import QuestionTheory
from MarkUp import MarkUp
from random import randint
import os


token = os.environ.get('API_TOKEN',None)
bot = TeleBot(token)
global phone_no, correct, incorrect_Point, correct_Point, markup, limit, mid, msgIncorrect_id

msgIncorrect_id=[]
incorrect_Point = 0
correct_Point = 0
limit = 0
correct=''
mid=0

markup =MarkUp([])

@bot.message_handler(commands='start')
def handler_on_start(message):
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_message(message.chat.id,f'Hello {message.from_user.first_name}!\n'
                                     f'Welcome to Theory practice.\n'
                                     f'For start please press /StartGame .')

def return_correct_answer():
    global correct
    return correct

def sendQuestion(call):
    global correct, markup, mid
    randomQ = randint(1,1274)
    theoryQ = QuestionTheory(randomQ)
    question, all_answers, correct_answer, img = theoryQ.get_question()
    print("Correct Answer is: "+correct_answer)
    correct = correct_answer
    markup = MarkUp(all_answers)
    if img!="No":
        mid = bot.send_photo(chat_id=call.chat.id,photo=img,caption='שאלה :\n'+question,reply_markup=markup.get_answers_Reoplybtn())
    else:
        mid = bot.send_message(chat_id=call.chat.id,text='שאלה :\n'+question,reply_markup =markup.get_answers_Reoplybtn())




@bot.message_handler(commands = ['StartGame','StartGame'.lower()])
def start_game(message):
    global markup
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, 'If you will want to finish write /Finish')
    bot.send_message(message.chat.id, 'start practice ...')
    bot.send_message(message.chat.id, 'The Practice in Hebrew.\n',
                     reply_markup=markup.create_understand_Replybtn())




@bot.message_handler(func=lambda call: True)
def answer_message_query(call):
    global incorrect_Point, correct_Point, limit, mid, msgIncorrect_id

    if call.text == "Ok, lets start" :
        sendQuestion(call)
    elif call.text == "/continue" :
        limit = 0
        sendQuestion(call)

    elif call.text == "/Finish":
        bot.send_message(call.chat.id,f"GoodBye {call.from_user.first_name} 👋 ",reply_markup= ReplyKeyboardRemove(True))

    elif limit > 29:
        bot.send_message(call.chat.id,f"You pass {limit - 1} Question.\n"
                                      f"Do you want continue? \n"
                                      f"/continue or /Finish",reply_markup= ReplyKeyboardRemove(True))

    elif call.text == return_correct_answer():

        correct_Point += 1
        bot.send_message(call.chat.id,f"EXCELLENT ! You have {correct_Point} Correct Answers. ")
        bot.delete_message(call.chat.id, mid.message_id)
        bot.delete_message(call.chat.id, call.message_id)
        if msgIncorrect_id != []:
            for id in msgIncorrect_id:
                bot.delete_message(call.chat.id,id)
                msgIncorrect_id.remove(id)
        sendQuestion(call)
        limit += 1

    else:
        incorrect_Point += 1
        bot.send_message(call.chat.id,f'You have {incorrect_Point} Mistakes, try again.')
        msgIncorrect_id.append(call.message_id)

bot.polling()
