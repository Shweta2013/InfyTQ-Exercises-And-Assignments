#OOPR-Assgn-13
class Classroom:
    classroom_list=[1,2,3,4,5]
    
    @staticmethod
    def search_classroom(class_room):
        if class_room in Classroom.classroom_list:
            return "Found"
        else:
            return -1

print(Classroom.search_classroom(1))