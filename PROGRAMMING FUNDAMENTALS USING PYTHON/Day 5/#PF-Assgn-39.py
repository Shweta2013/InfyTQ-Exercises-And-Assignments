#PF-Assgn-39

#This verification is based on string match.     

#Global variables
menu=("Veg Roll","Noodles","Fried Rice","Soup")
quantity_available=[2,200,3,0]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    for i in range(0,len(item_tuple),2):
        if item_tuple[i] not in menu:
            print(item_tuple[i]+"is not available")
        else:
            if(check_quantity_available(menu.index(item_tuple[i]),item_tuple[i+1])):
                print (item_tuple[i]+" is available")
            else:    
                print(item_tuple[i]+" stock is over")
    
def check_quantity_available(index,quantity_requested):
    if(quantity_requested<=quantity_available[index]):
        quantity_available[index]-=quantity_requested
        return True
    return False

#Provide different values for items ordered and test your program
#place_order("Veg Roll",2,"Noodles",2)
#print()
place_order("Fried Rice",2,"Soup",1)