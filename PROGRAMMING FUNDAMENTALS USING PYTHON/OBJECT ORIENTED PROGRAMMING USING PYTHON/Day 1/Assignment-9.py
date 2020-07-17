course={1001:25575.0,1002:15500}
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__fees=None
        self.__course_id=None
    
    def get_student_id(self):
        return self.__student_id
    
    def get_marks(self):
        return self.__marks
    
    def get_age(self):
        return self.__age
    
    def set_student_id(self,student_id):
        self.__student_id=student_id
    
    def set_marks(self,marks):
        self.__marks=marks
    
    def set_age(self,age):
        self.__age=age
    
    def get_course_id(self):
        return self.__course_id
    
    def get_fees(self):
        return self.__fees
    
    def validate_marks(self):
        if self.get_marks()>=0 and self.get_marks()<=100:
            return True
        else:
            return False
    
    def validate_age(self):
        if self.get_age()>20:
            return True
        return False
    
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.get_marks()>=65:
                return True
            return False
        return False
    
    
    def choose_course(self,course_id):
        if course_id in course.keys():
            self.__course_id=course_id
            if self.get_marks()>85:
                self.__fees=course[course_id]*0.75
            else:
                self.__fees=course[course_id]*1.0
            return True
        else:
            return False
            
maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(100)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")