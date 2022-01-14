from bs4 import BeautifulSoup
from telebot import TeleBot
import os
import re
import requests



class User():

    def __init__(self, user_name, user_id):

        self.user_name = user_name
        self.user_id = user_id

        self.POSTER_TOKEN = os.environ.get('API_TOKEN_POSTERBOT',None)

        self.channel_id = os.environ.get('CHANNEL_ID',None)

        self.post_bot = TeleBot(self.POSTER_TOKEN)

        self.USERNAME_CHANNEL = os.environ.get('USERNAME_CHANNEL',None) 

        self.URL_CHANNEL = f'https://t.me/s/{self.USERNAME_CHANNEL}'


    def POST_ON_CLOUD(self):
        self.post_bot.send_message(self.channel_id,f'{self.user_name}\nuser_id : {self.user_id}')

    def GET_FROM_CLOUD(self,username):
        user_lst = []
        response = requests.get(self.URL_CHANNEL)
        soup = BeautifulSoup(response.text, 'html.parser')
        message = soup.find_all('div', {'class': 'tgme_widget_message_text js-message_text'})

        for classes in message:

            if 'user_id' in classes.text:
                a = re.split('user_id| : ', classes.text)
                a.remove('')
                user_lst.append(a)
        for user in user_lst:
            if user[0] == username :
                return True





