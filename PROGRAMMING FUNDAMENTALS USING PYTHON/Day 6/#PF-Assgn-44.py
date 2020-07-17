#PF-Assgn-44

def find_duplicates(list_of_numbers):
    list_of_duplicates=[]
    for i in list_of_numbers:
        if i not in list_of_duplicates and list_of_numbers.count(i)>1:
            list_of_duplicates.append(i)
        else:
            continue
    return list_of_duplicates
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)