#PF-Assgn-40

def is_palindrome(word):
    if(word[::-1].lower()==word.lower()):
        return True
    else:
        return False

#Provide different values for word and test your program
result=is_palindrome("abba")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")