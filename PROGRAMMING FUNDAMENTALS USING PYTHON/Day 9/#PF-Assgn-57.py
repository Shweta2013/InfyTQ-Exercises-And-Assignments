#PF-Assgn-57

def check_prime(number):
    flag=False
    if number > 1:  
        for i2 in range(2,number+1):  
            if number%i2==0 and i2!=number:  
                flag=False
                break  
            else:  
                flag=True
        return flag
    else:  
       return False

def rotations(num):
    rotations=[]
    num=str(num)
    for i3 in range(0,len(num)):
        if(i3==0):
            number=num[i3]+num[i3+1:]
        else:    
            number=num[i3]+num[i3+1:]+num[0:i3]
        rotations.append(int(number))
    return rotations

def get_circular_prime_count(limit):
    pass #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    circular_prime=0
    for i in range(1,limit):
        list_of_rotations=rotations(i)
        count=0
        for i1 in range(0,len(list_of_rotations)):
            if (check_prime(list_of_rotations[i1])):
                count+=1
            else:
                continue
        if(count==len(list_of_rotations)):
            circular_prime+=1
        else:
            continue
    return circular_prime
            
#Provide different values for limit and test your program
print(get_circular_prime_count(7))