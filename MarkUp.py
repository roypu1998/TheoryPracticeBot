from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup

class MarkUp:
    def __init__(self,lst):
        self.lstAnswers = lst

    def get_answers_Inlinebtn(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 4
        for i in range(4):
            markup.add(InlineKeyboardButton(self.lstAnswers[i],callback_data=str(i)))

        return markup

    def create_understand_Inlinebtn(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1

        markup.add(InlineKeyboardButton("Ok, let's start",callback_data="ok"))

        return markup


    def create_understand_Replybtn(self):
        markup = ReplyKeyboardMarkup()
        string = 'Ok, lets start'
        markup.row(string)
        markup.row('/Finish')
        markup.row('')

        return markup

    def get_answers_Reoplybtn(self):
        markup = ReplyKeyboardMarkup()
        for ans in self.lstAnswers:
            markup.row(ans)
        return markup
