#PF-Assgn-33

def find_common_characters(msg1,msg2):
    output_string=""
    for letter1 in msg1:
        if letter1 in msg2:
            if letter1 in output_string:
                continue
            else:
                output_string=output_string+letter1
    if(len(output_string)==0):
        return -1

    return output_string
    
#Provide different values for msg1,msg2 and test your program
msg1="Apple"
msg2="Moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)