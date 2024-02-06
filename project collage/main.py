from collage import Collage
from collage_manegment import *
from staff import Staff
from lecturer import Lecturer

def main():
    
    ceo = Staff("amnon titinsky", 10000, 25, "0567489304", None, "CEO", 2000)
    offisial_academy = Collage("hebrow academic", ceo)
    k = Collage_manegment(offisial_academy)



    print(k.WELLCOME_MESSAGE)
    while True:
        print(k.INSTRUCTION_COMMEND)
        com = input("""
                    1. log in as an ADMIN
                    2. log in as a LECTRUR
                    3. log in as a STUDENT
                    4. log in as a GUEST
                    5. log in as the system menager
                    """)
        
        if com == "1":
            k.admin_page()

        elif com == "2":
            k.lecturer_page()

        elif com == "3":
            k.student_page()

        elif com == "4":
            # FIXME 
            k.guest_page()

        elif com == "5":
            k.menager_system_page()

        else:
            pass

if __name__ == "__main__":
    main()