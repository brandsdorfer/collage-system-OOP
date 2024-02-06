from staff import Staff
from presence import Presence

class Lecturer(Staff):

    def __init__(self, name: str, id: int, age: int, phone_num: str, addres: list, role: str, salary_per_hour: int, prefession):
        super().__init__(name, id, age, phone_num, addres, role, salary_per_hour)
        self._prefession = prefession
        self._presence = Presence()
        self._corse = []
    
    @property
    def profession(self):
        return self.profession
    
    def show_corses(self):
        for i in self._corse:
            print(f"""
                corse {i.name},
                there is {i.sum_of_students} students.""")
    
    def add_course(self, cours):
        self._corse.append(cours)