#OOPR-Assgn-20
class Applicant:
    __application_dict={"A":2,"B":4,"C":5,"D":3}
    __applicant_id_count=1000
    
    def __init__(self,applicant_name):
        self.__applicant_name=applicant_name
        self.__applicant_id=None
        self.__job_band=None
    
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict
    
    def get_applicant_id(self):
        return self.__applicant_id
        
    def get_applicant_name(self):
        return self.__applicant_name
    
    def get_job_band(self):
        return self.__job_band
    
    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1
        self.__applicant_id=Applicant.__applicant_id_count
        
    def apply_for_job(self,job_band):
        count=Applicant.__application_dict.get(job_band)
        if count==5:
            return -1
        else:
            Applicant.__application_dict[job_band]=count+1
        self.generate_applicant_id()
        self.__job_band=job_band
        
        
applicant=Applicant("Shweta")
if applicant.apply_for_job("A")!=(-1):
    print(applicant.get_applicant_id())
    print(applicant.get_applicant_name())
    print(applicant.get_job_band())
else:
    print("Application is not accepted (applicant count exceeded)")
print(applicant.get_application_dict())