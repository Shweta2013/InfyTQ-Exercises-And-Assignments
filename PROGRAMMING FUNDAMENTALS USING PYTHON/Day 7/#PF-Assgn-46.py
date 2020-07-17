#PF-Assgn-46

import sys
def nearest_palindrome(number):
    #start writitng your code here
    for i in range(number+1,sys.maxsize):
        num1=str(i)
        if(num1==num1[::-1]):
            return num1

number=99
print(nearest_palindrome(number))