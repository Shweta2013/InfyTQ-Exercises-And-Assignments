#PF-Assgn-30

def encode(message):
    string=""
    count=1
    for l in range(1,len(message)):
        if(message[l]==message[l-1]):
                count+=1
        else:
            string+=str(count)+message[l-1]
            count=1
        
    return string
               

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)