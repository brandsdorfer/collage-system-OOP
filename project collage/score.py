class Score():

    def __init__(self, person, course):
        self._person = person
        self._course = course
        self._score = {}
    
    @property
    def score(self):
        return self._score
    
    def add_to_score(self, name_test, score):
        self._score[name_test] = score

    def show_total_score(self):
        if len(self._score) == 0:
            print(f"there is no scores for student {self._person.name} in course {self._course.name}")
            return
        total_score, length = 0, 0
        for value in self._score:
           total_score += value
           length += 1
       
        total_score = (total_score / length)
        print(f"the scores for student {self._person.name} in course {self._course.name} is:\n{total_score}")
        return total_score
       