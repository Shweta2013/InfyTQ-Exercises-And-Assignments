#PF-Assgn-48

def find_correct(word_dict):
    CORRECT=0
    ALMOST_CORRECT=0
    WRONG=0
    list_of_answers=[0,0,0]
    #start writing your code here
    for key in word_dict:
        if(key==word_dict[key]):
            CORRECT+=1
            list_of_answers[0]=CORRECT 
        else:
            
            if(len(key)==len(word_dict[key])):
                matched_letter=0
                for letter in key:
                    if letter in word_dict[key]:
                        matched_letter+=1
                
                if(matched_letter>=len(key)-2):
                    ALMOST_CORRECT+=1
                    list_of_answers[1]=ALMOST_CORRECT
                else:
                    WRONG+=1
                    list_of_answers[2]=WRONG
            else:
                WRONG+=1
                list_of_answers[2]=WRONG
        '''for k,v in word_dict.items():
            if len(k)==len(v):'''
        
    return list_of_answers

word_dict={"WHIZZY":"MIZZLY","PRETTY":"PRESEN"}
print(find_correct(word_dict))