#DSA-Assgn-19

def last_instance( num_list,  start,  end,  key):
    if key in num_list:
        for i in range(start,end+1):
            if num_list[i]==key:
                last_occurance=i
        return last_occurance
    else:
        return -1

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=1 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")