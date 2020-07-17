#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    sum1=0
    for i in sample_data:
        sum1=sum1+i
    return sum1
   
    
def even(data):
    e1=[]
    for e in sample_data:
        if(e%2==0):
            e1.append(e)
    return e1
   
   
def odd(data):
    o1=[]
    for o in sample_data:
       if(o%2!=0):
           o1.append(o)
    return o1

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))