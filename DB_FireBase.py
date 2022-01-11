from firebase import firebase
import os

class User():
    def __init__(self,user_name,user_id):
        self.username = user_name
        self.user_id = user_id
        self.DB_URL = os.environ.get('FireBaseURL',None)
        self.app = firebase.FirebaseApplication(self.DB_URL, None)

    def PutOnDatabase(self):
        self.app.put("",self.username,data={"User Id" : self.user_id})

    def GetFromDatabase(self,user_name):
        userDict = self.app.get(url="",name="",connection=None)
        flag = False
        if userDict != None:
            if user_name in userDict.keys():
                flag = True

        return flag

#app = firebase.FirebaseApplication('https://users-a9d23-default-rtdb.firebaseio.com/', None)

