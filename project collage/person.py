import addres
from presence import Presence
class Person():

    def __init__(self, name:str, id:int, age:int, phone_num:str, addres:list = []):
        self._name = name
        self._id = id
        self._age = age
        self._phone_num = phone_num
        self._addres = addres
        
        self._presence = Presence()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def age(self):
        return self._age
    
    @property
    def id(self):
        return self._id
    
    def presence_system(self):
        print("WELCOME TO THE PRESENCE SYSTEM")
        print(f"""
    hello {self.name}.
    now you enter your presence system
""")
        self._presence.update()