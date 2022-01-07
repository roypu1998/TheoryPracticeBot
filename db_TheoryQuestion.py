import requests
from bs4 import BeautifulSoup as bs

class QuestionTheory():

    def __init__(self,question_no):

        self.quest_no = question_no
        self.url = "https://teo.co.il/questions/b"

    def get_question(self):
        url = self.url + '/' + str(self.quest_no)
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        question = soup.find('h3').get_text()
        li_tags = soup.find("section", {"id": "main-self"}).find('ul').find_all('li')
        dictAnswers = {}

        for li in li_tags:
            lst = li.get_text().split('\n')

            for s in lst:
                if s != '':
                    dictAnswers[s] = li.find('input').get('data-correct')
        if soup.find('img') != None:
            dictAnswers['image'] =  soup.find('img').get('src')
            img=dictAnswers['image']
        else:
            dictAnswers['image'] = 'No'
            img='No'
        all_answers=[]
        for k,v in dictAnswers.items():
            if k != 'image':
                all_answers.append(k)
            if v == '1':
                correct_answer = k


        return question,all_answers,correct_answer, img





