from datetime import datetime

class Spy:


    def __init__(self,name,salutation,age,rating):
        self.sal=salutation
        self.name=self.sal+' '+name
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.current_status=None


spy=Spy('Anjali','Ms.',21,3.7)
class chatmessage:
    def __init__(self,message,st):
        self.msg=message
        self.time=datetime.now()
        self.send_by_me=st