#PF-Assgn-34

def find_pairs_of_numbers(num_list,n):
    count=0
    for number1 in num_list:
        for number2 in num_list:
            if(number1+number2==n):
                count+=1
    count//=2
    return count
                
num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))