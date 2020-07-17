#PF-Assgn-42

sum_of_factors=0
def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0 and is_prime(i,i/2)):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(int(i)==1):
        return True
    elif(num%int(i)==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    #Accepts the list of factors and returns the largest prime factor
    largest_factor=max(list_of_factors)
    return largest_factor

def find_f(num):
    #Accepts the number and returns the largest prime factor of the number
    
    largest_prime_factor=find_largest_prime_factor(find_factors(num))
    return largest_prime_factor

def find_g(num):
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    global sum_of_factors
    for i in range(0,9):
        sum_of_factors+=find_f(num+i)
    return sum_of_factors

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))