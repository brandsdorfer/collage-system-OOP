from person import Person
from score import Score
from presence import Presence

class Student(Person):

    def __init__(self, name: str, id: int, age: int, phone_num: str, addres: list):
        super().__init__(name, id, age, phone_num, addres)
        self._courses = []
        self._scores = []

    @property
    def list_of_courses(self):
         return self._courses
    @property
    def sumOfcourses(self):
        return len(self._courses)
    
    def update_score(self, name_course, score):
        self._scores[name_course] = score
    
    def get_ave_score(self):
        total_score = sum(self._scores.values())
        return (total_score / len(self._scores))
    
    def add_corse(self, corse):
        new_score = Score(self, corse)
        self._scores.append(new_score)
        self._courses.append(corse)

    def print_student(self, i): 
            print(f"""
            {i}. name: {self.name}
                the age of student {self.age}
                nom of his course {self.sumOfcourses}:
                -----\n""") 
    
    def show_all_scores(self):
        if len(self._scores) > 0:
            for score in self._scores:
                score.show_total_score()
        else:
            print("there is no scores for the student")

    def total_score_for_student(self):
        if len(self._scores) > 0:
            k = 0
            print("in process...")
            for score in self._scores:
                k += score.show_all_courses()
            print(f"TOTAL SCORE:\n {k/len(self._scores)} present from {len(self._scores)} courses")
        else:
            print("there is no scores for the student")