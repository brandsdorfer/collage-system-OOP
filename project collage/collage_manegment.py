from lecturer import Lecturer
from student import Student
from course import Course

class Collage_manegment():

     WELLCOME_MESSAGE = """

                     ==========================
                   ;/|\  /                  \  /|\;
                         |__________________|


                    ############################
                    #                          #
                    #  ######################  #
                    #  #                    #  #
                    #  #  COLLAGE SYSTEM    #  #
                    #  #                    #  #
                    #  ######################  #
                    #          ~jcs~           #
                    ############################
                    
                    
                    WELLCOME TO THE COLLAGE SYSTEM!!!
                    """
     VALITETION_ERROR = "ERROR!\nyou enter an invalid commend.\n"

     INSTRUCTION_COMMEND = "press acoording to the below commends"

     def __init__(self, collage):
          self._collage = collage

     def admin_page(self):
          while True:
               com = input("""
                         1. add a new student to collage
                         2. add a student to course
                         3. create a new course
                         4. exit
                         """)
               if com == "1":
                    self._collage.add_a_student_in_ui() 

               elif com == "2":
                    self._collage.add_student_to_course_id()

               elif com == "3":
                    self._collage.add_new_corse()

               elif com == "4":
                    return
               else:
                   print(Collage_manegment.VALITETION_ERROR)          

     def lecturer_page(self):
          enter_id = input("welcome to the lecturer portal\nplaese entee your id number :")
          lect_obj = self._collage.check_lecturer_by_id(enter_id)
          if lect_obj != False:
               lect_obj.print_student("your details is")
               while True:
                    ask_stu = input(f"""
                    hello {lect_obj.name}! press according to the below commends:
                    1. to see your course
                    2. 
                    3. 
                    4. to update score for student
                    5. to exit
                    """)
                    if ask_stu == "1":
                         lect_obj.show_all_courses()
                    elif ask_stu == "2":
                         pass
                    elif ask_stu == "3":
                         pass
                    elif ask_stu == "4":
                         course_name = input("enter the name of the course :")
                         
                    elif ask_stu == "5":
                         return
                    else:
                         print("not valid commend")
          else:
               print("there is no a lecturer with this id\n")


     def student_page(self):
          enter_id = input("plaese entee your id number :")
          stu_obj = self._collage.check_student_by_id(enter_id)
          if stu_obj != False:
               stu_obj.print_student("your details is")
               while True:
                    ask_stu = input(f"""
                    hello {stu_obj.name}! press according to the below commends:
                    1. to join a new course
                    2. to see you all courses
                    3. to see your score
                    4. to enter you presence system
                    5. to exit
                    """)
                    if ask_stu == "1":
                         course_name = input("enter the name of the course :")
                         self._collage.add_student_to_course(enter_id, course_name)
                    elif ask_stu == "2":
                         self._collage.show_all_courses(stu_obj)
                    elif ask_stu == "3":
                         stu_obj.show_all_scores()
                    elif ask_stu == "4":
                         stu_obj.presence_system()
                    elif ask_stu == "5":
                         return
                    else:
                         print("not valid commend")
          else:
               print("there is no a student with this id\n")

     def guest_page(self):
          while True:
               com = int(input("""
                         1. see all students
                         2. see all courses
                         3. see the collage details
                         4. exit
                         """))
               if com == 1:
                    self._collage.show_all_students()
               elif com == 2:
                    self._collage.show_all_courses()
               elif com == 3:
                    self._collage.print_collage_dadiels()
               elif com == 4:
                    return
               else:
                   print(Collage_manegment.VALITETION_ERROR)
                    
     def menager_system_page():
          pass