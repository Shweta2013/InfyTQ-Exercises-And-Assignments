#PF-Assgn-31

def check_palindrome(word):
    if(word[::-1]==word):
        return True
    else:
        return False
        
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")