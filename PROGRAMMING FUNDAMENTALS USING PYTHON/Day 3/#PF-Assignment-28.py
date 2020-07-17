#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    sum_of_digits=0
    list_of_numbers=[]
    if(num1<num2):
        for i in range(num1,num2+1):
            number=i
            while(i!=0):
                remainder=i%10
                sum_of_digits+=remainder
                i//=10
            if(sum_of_digits%3==0 and number%5==0):
                num_str=str(number)
                if(len(num_str)==2):
                    list_of_numbers.append(number)
            sum_of_digits=0
        if(len(list_of_numbers)!=0):        
            max_num=max(list_of_numbers)
    else:
        max_num=-1
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(2,14)
print(max_num)