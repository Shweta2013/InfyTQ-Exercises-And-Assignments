#PF-Assgn-56

def max_frequency_word_counter(data):
    word=""
    frequency=0
    new1={}
    word_list=[]
    new_text=data.upper().split()
    
    for i in new_text:
        count=new_text.count(i)
        new1[i]=count
    
    
    value=list(new1.values())
    value.sort(reverse=True)
    key=list(new1.keys())
    
    frequency=value[0]
    for i in new1:
        if new1[i]==frequency:
            word_list.append(i)
    word=word_list[0]
    for i in range(1,len(word_list)):
        if len(word_list[i])>len(word):
            word=word_list[i]
    print(word,frequency)
  
#Provide different values for data and test your program.
data="Listen to the big clock Tick tock tick" 
max_frequency_word_counter(data)