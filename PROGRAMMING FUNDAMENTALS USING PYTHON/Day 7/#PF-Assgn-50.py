#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    splitted_data=data.split()
    consonents=""
    for word in splitted_data:
        if len(word)==1:
            consonents+=word
        for letter in word:
            if letter not in "aeiouAEIOU":
                consonents+=letter
        consonents+=" "
    
    return consonents[:len(consonents)-1]
data="I love Python"
print(sms_encoding(data))