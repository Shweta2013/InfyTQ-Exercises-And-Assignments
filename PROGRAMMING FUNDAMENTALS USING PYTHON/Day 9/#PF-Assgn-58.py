#PF-Assgn-58

def validate_credit_card_number(card_number):
    #start writing your code here
    card_number_list=[int(i) for i in str(card_number)]
    
    '''even_index=[]
    odd_index=[]
    for i in range(0,len(card_number_list)):
        if i%2==0:
            even_index.append(card_number_list[i])
        elif i%2==1:
            odd_index.append(card_number_list[i])
    print(card_number_list)
    print(even_index)
    print(odd_index)'''
    if len(card_number_list)==16:
        sum1=sum(card_number_list)
        print(sum1)
        if sum1%10==0:
            return True
        return False
    return False
    
card_number=1456734512345698 #5239512608615007 #4539869650133101 

result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")