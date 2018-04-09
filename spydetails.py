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
class Chats:
    def __init__(self,time,sender,message,receiver):
        self.time=time
        self.sender=sender
        self.msg=message
        self.receiver=receiver