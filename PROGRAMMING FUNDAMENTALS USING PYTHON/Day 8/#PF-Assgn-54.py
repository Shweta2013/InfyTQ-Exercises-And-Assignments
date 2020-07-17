#PF-Assgn-54

def check_anagram(data1,data2):
    #start writing your code here
    anagram=[]
    anagram1=[]
    len_data1=len(data1)
    len_data2=len(data2)
    data1_upper= data1.upper()
    data2_upper= data2.upper()
    
    if(len_data1==len_data2):
        for letter in data1_upper:
            if letter in data2_upper:
                if(data1_upper.index(letter)!=data2_upper.index(letter)):
                    anagram.append("True")
                else:
                    anagram.append("False")
            else:
                return False
                
        for letter in data2_upper:
            if letter in data1_upper:
                if(data2_upper.index(letter)!=data1_upper.index(letter)):
                    anagram1.append("True")
                else:
                    anagram1.append("False")
            else:
                return False
        
        if ("False" not in anagram and "False" not in anagram1):
            return True
        else:
            return False
    
    else:
        return False
        

print(check_anagram("listen","silent"))