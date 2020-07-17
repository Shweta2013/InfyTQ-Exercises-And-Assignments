#PF-Assgn-61

def validate_name(name):
    if name=="" or len(name)>15 or name==" ":
        print("Invalid Name")
        return False
    if(type(name)=="number"):
        print("Invalid Name")
        return False
    return True
        
def validate_phone_no(phone_no):
    if(len(phone_no)==10):
        if(phone_no.isdigit()):
            if (phone_no.count(phone_no[0]))==len(phone_no):
                print("Invalid phone number")
                return False
            return True
            
        print("Invalid phone number")
        return False

    print("Invalid phone number")
    return False
            

def validate_email_id(email_id):
    if email_id.count("@")==1 and email_id.count(".com")==1:
        if email_id.endswith(".com"):
            if "gmail" in email_id or "yahoo" in email_id or "hotmail" in email_id:
                return True
            
            print("Invalid email id")
            return False
    
        print("Invalid email id")
        return False
   
    print("Invalid email id")
    return False
            
                
def validate_all(name,phone_no,email_id):
    if validate_name(name) and validate_phone_no(phone_no) and validate_email_id(email_id):
        print("All the details are valid")
        
#Provide different values for name, phone_no and email_id and test your program
validate_all("", "99qw23344@", "tina@yahoo.com")