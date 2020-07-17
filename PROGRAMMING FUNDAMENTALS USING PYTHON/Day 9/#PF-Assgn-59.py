#PF-Assgn-59

def check_perfect_number(number):
    divisors_sum=0
    for i in range(1,number):
        if(number%i==0):
            divisors_sum+=i
    if divisors_sum==number:
        return True
    return False
        
def check_perfectno_from_list(no_list):
    perfect_no=[]
    for element in no_list:
        if check_perfect_number(element) and element!=0:
            perfect_no.append(element)
    return perfect_no

perfectno_list=check_perfectno_from_list([87, 76, 567, 99, 0])
print(perfectno_list)