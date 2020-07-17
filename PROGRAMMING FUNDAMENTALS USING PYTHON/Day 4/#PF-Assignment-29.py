#PF-Assgn-29
def calculate(distance,no_of_passengers):
    #Remove pass and write your logic here
    mileage=10
    amount=(no_of_passengers*80)-(distance/mileage)*70
    if(amount<0):
        return -1
    else:
        return amount



#Provide different values for distance, no_of_passenger and test your program
distance=30
no_of_passengers=2
print(calculate(distance,no_of_passengers))