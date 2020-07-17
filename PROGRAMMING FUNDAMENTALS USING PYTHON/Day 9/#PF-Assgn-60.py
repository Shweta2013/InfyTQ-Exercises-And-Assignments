#PF-Assgn-60

def remove_duplicates(value):
    #start writing your code here
    result=[]
    list_of_string=[letter for letter in value]
    for letter in list_of_string:
        if letter not in result:
            result.append(letter)
    return str("".join(result))
            
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))