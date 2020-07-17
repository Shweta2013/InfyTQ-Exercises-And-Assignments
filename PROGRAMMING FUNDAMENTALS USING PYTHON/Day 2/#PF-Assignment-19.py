#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if(quantity_ordered>=1 and distance_in_kms>0):
        if(food_type=='N'):
            if(distance_in_kms<=3):
                bill_amount+=150*quantity_ordered
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount+=150*quantity_ordered+3*(distance_in_kms-3)
            elif(distance_in_kms>6):
                bill_amount+=150*quantity_ordered+6*(distance_in_kms-6)+9
        elif(food_type=='V'):
            if(distance_in_kms<=3):
                bill_amount+=120*quantity_ordered
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount+=120*quantity_ordered+3*(distance_in_kms-3)
            elif(distance_in_kms>6):
                bill_amount+=120*quantity_ordered+6*(distance_in_kms-6)+9
        
        else:
            bill_amount=-1
    else:
        bill_amount=-1
        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",1,7)
print(bill_amount)