#PF-Assgn-23

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    avail=[]
    
    #Write your logic here
    if 0 not in reqd_quantity:
        for gem in reqd_gems:
            if gem in gems_list:
                avail.append("True")
            else:
                avail.append("False")
            
        if "False" in avail:
            bill_amount=-1
        else:
            i=0
            for gem in reqd_gems:
                gem_index=gems_list.index(gem)
                gem_price=price_list[gem_index]
                gem_quant=reqd_quantity[i]
                bill_amount+=gem_quant*gem_price
                i+=1
    if(bill_amount>30000):
        bill_amount=bill_amount-(bill_amount*0.05)
    return bill_amount

#List of gems available in the store
gems_list=["Amber","Aquamarine","Opal","Topaz"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[4316,1342,8734,6421]

#List of gems required by the customer
reqd_gems=["Amber","Topaz"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[1,4]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)