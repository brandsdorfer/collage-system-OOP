from student import Student

class Course():

    def __init__(self, course_name, lecturer):
        self._course_name = course_name
        self._lecturer = lecturer
        self._score_for_student = {}
        self.list_of_students = []

    @property
    def name(self):
        return self._course_name
    
    @property
    def lecturer(self):
        return self._lecturer

    def add_student(self, student):
        self.list_of_students.append(student)
        student.add_corse(self)

    def update_score_for_student(self, student_id, score:int):
        self._score_for_student[student_id] += score

    def get_score_for_student(self, student_id):
        return self._score_for_student[student_id]
    
    def change_lecturer(self, new_lecturer):
        self._lecturer = new_lecturer

    def sum_of_students(self):
        return len(self.list_of_students)