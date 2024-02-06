from person import Person

class Staff(Person):

    def __init__(self, name: str, id: int, age: int, phone_num: str, addres: list, role:str, salary_per_hour:int):
        super().__init__(name, id, age, phone_num, addres)
        self._role = role
        self._salary_per_hour = salary_per_hour
        self._work_time = {"Sunday":None, "Monday":None, "Tuesday":None, "Wednesday":None, "Thursday":None, "Friday":None, "Saturday":None,}
        self._presence = {}

    @property
    def role(self):
        return self._role
    
    @property
    def salary_per_hour(self):
        return self._salary_per_hour
    
    @salary_per_hour.setter
    def salary_per_hour(self, new_sum):
        self._salary_per_hour = new_sum

    def get_work_time(self, day):
        return self._work_time[day]
    
    def update_work_time(self, day, new_hour):
        self._work_time[day] = new_hour