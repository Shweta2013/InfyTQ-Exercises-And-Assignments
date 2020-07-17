#PF-Assgn-38

def check_double(number):
    str1=(str(number))
    str2=(str(number*2))
    boolean=[]
    
    if (len(str1)==len(str2)):
        for digit in str1:
            if digit in str2:
                boolean.append("True")
            else:
                boolean.append("False")
    else:
        return False
    if "False" not in boolean:
        return True
    else:
        return False
                
print(check_double(125874))