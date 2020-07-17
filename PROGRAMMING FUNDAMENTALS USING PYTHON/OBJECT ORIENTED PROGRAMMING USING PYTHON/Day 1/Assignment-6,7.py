class Instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__experience=None
        self.__avg_feedback=None
        self.__technology_skill=None
    
    def get_instructor_name(self):
        return self.__instructor_name
    
    def get_experience(self):
        return self.__experience
        
    def get_avg_feedback(self):
        return self.__avg_feedback
        
    def get_technology_skill(self):
        return self.__technology_skill
    
    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
    
    def set_experience(self,experience):
        self.__experience=experience
    
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
        
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
        
    def check_eligibility(self):
        if (self.get_experience()>3 and self.get_avg_feedback()>=4.5) or (self.get_experience()<=3 and self.get_avg_feedback()>=4.0):
            return True
        else:
            return False
            
    def allocate_course(self,technology):
        if self.check_eligibility():
            if technology in self.get_technology_skill():
                return True
            else:
                return False
        else:
            return False