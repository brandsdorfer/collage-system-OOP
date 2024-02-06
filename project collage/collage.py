from database.database_pro import insart_student
from student import Student
from staff import Staff
from course import Course
from lecturer import Lecturer
from collage_manegment import *

class Collage():

    def __init__(self, collage_name, ceo, addres=None):
        self._collage_name = collage_name
        self._ceo = ceo
        self._addres = addres
        self._list_of_staff = []
        self._list_of_lectrers = [Lecturer("avi levi", 10005, 33, "098857643", None, "lectuere", 200, "learning python")]
        self._list_of_students = [Student("yoel", 10001, 23, "09827465", None), Student("yaakov rat", 10002, 43, "048356627", None), Student("moshe cohen", 10003, 36, "09877663452", None)]
        self._list_of_courses = [Course("python CS", self._list_of_lectrers[0])]
   

    @property
    def name(self):
        return self._collage_name

    @property
    def ceo(self):
        return self._ceo.name

    @property
    def list_of_courses(self):
        return self._list_of_courses

    @property
    def list_of_students(self):
        return self._list_of_students
    
    # checking
    
    def check_course_by_name(self, course_name):
        for course in self._list_of_courses:
            if course.name == course_name:
                return course 
        return False

    def check_student_by_id(self, student_id: str):
        for student in self.list_of_students:
            if student.id == int(student_id):
                return student    
        return False
    
    def check_lecturer_by_id(self, id:str):
        for lectuere in self._list_of_lectrers:
            if lectuere.id == int(id):
                 return lectuere
        return False
    

    # adding 

    def add_student(self, student_id, name, age, phone_nom, addres=None):
            if self.check_student_by_id(student_id) == False:
                new_student = Student(name=name, id=student_id, age=age, phone_num=phone_nom, addres=addres)
                self.list_of_students.append(new_student)
                return "student added succefully"
            else:
                return "student is already in collage"
    

    def add_new_corse(self):
          try:
               name = input("please enter the name of course")

               ask_lecturer = input("you want to add a new lecturer ? (write 'YES' if you want) :")
               lecturer = Lecturer("moshe", 453627, 23, "056738425", None, "learning", 120, None, None)
               if ask_lecturer == "YES":
                    lecturer = self.add_lecturer()

               new_corse = Course(name , lecturer)
               lecturer.add_course(new_corse)
               print(self.create_course(new_corse))
          except Exception:
               print(Collage_manegment.VALITETION_ERROR)

    def add_student_to_course(self, student_id, course_name):
        course = self.check_course_by_name(course_name)
        student = self.check_student_by_id(student_id)
        if course and student != False:
            course.add_student(student)
            print(f"student {student.name} added succefuly to course {course.name}")
        else:
             print(Collage_manegment.VALITETION_ERROR, "\none of the details or more are invalid!")   

    def add_lecturer(self, lecturer):
        self._list_of_lectrers.append(lecturer)
        
    def remove_student(self, student_id):
        student_valid = self.get_student_by_id(student_id)
        if student_valid != False:
            self.list_of_students.remove(student_valid)
                
    def create_course(self, course):
        if self.check_course_by_name(course.name) == False:
            self._list_of_courses.append(course)
            return "course added succefully"
        else:
            return "course is alraedy created"


    def add_student_to_course_id(self):
            inps = input('enter the id of the student :')
            inp = input('enter the name of course :')
            self.add_student_to_course(inps, inp)

    def show_all_students(self, is_corse: bool or Course=False):
          list_of_students = self.list_of_students
          if is_corse != False:
               list_of_students = is_corse.list_of_students
              
          print(f"""here is the list of all students in {self.name}:
               press num of student to see more details...\n""")
          for i in range(1, len(list_of_students)+1):
               student = list_of_students[i-1]
               student.print_student(i)
          
               if student.sumOfcourses > 0:
                    self.show_all_courses(student)
    
    def show_all_courses(self, is_student: bool or Student=False):
          if is_student != False:
               courses = is_student.list_of_courses
          else:
               courses = self.list_of_courses
          
          if len(courses) == 0:
               print("there is no courses to show")
               return

          for i in range(len(courses)):
               course = courses[i]
               print(f"""
                    ------
                         * {course.name},
                         * {course.lecturer.name} is the lecturer,
                         * there is {len(course.list_of_students)} students in the course
                    ------\n""")


    def get_details(self, role:str):
        student_id = input(f"add a new {role}!\n enter the {role} id :")
        name = input(f"enter the name of {role}:")
        age = int(input(f"enter the age {role}:"))
        phone_nom = input(f"enter a phone number {role}:")
        return (student_id, name, age, phone_nom)
    
    def add_a_student_in_ui(self):
        try:
            details_ui = self.get_details("student")
            print(self.add_student(details_ui[0], details_ui[1], details_ui[2], details_ui[3]))
            return
        except ValueError:
            print(Collage_manegment.VALITETION_ERROR)
            return

    def add_lecturer(self):
          try:
               details_per = self.get_details("lecturer")
               proffision = input("what is the lecturer profession? :")
               new_lecturer = Lecturer(details_per[0], details_per[1], details_per[2], details_per[3], None, "lecturer", None, None, proffision)
               self.add_lecturer(new_lecturer)
               print("|~~|  the lecturer is added succefuly!")
               return new_lecturer
          except Exception:
               print(Collage_manegment.VALITETION_ERROR)   
    

    # collage functions    
    def print_collage_dadiels(self):
                print(f"""
        this collage is {self.name}:
        and there is {len(self.list_of_students)} students:
        {len(self.list_of_courses)} courses:
        {len(self._list_of_lectrers)} lecturers:
        ///// ////////  ///// ///
        """)