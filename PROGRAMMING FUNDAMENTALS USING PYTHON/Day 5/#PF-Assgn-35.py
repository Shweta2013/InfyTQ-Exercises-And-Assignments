#PF-Assgn-35

#no_of_students=10
#Global variable
list_of_marks=(0,0,0,0,0,0,0,0,0,0)

def find_more_than_average():
    count=0
    mark_avg=sum(list_of_marks)/len(list_of_marks)
    for num in list_of_marks:
        if num>mark_avg:
            count+=1
    return (count/10)*100
    

def sort_marks():
    list_tuple=list(list_of_marks)
    list_tuple.sort()
    return list_tuple

def generate_frequency():
    frequency=[]
    for i in range(0,26):
        value=list_of_marks.count(i)
        frequency.append(value)
    return frequency

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())