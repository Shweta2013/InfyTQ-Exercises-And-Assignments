#OOPR-Assgn-12
class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=None
    
    def get_bill_id(self):
        return self.__bill_id
        
    def get_patient_name(self):
        return self.__patient_name
    
    def get_bill_amount(self):
        return self.__bill_amount
    
    def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
        total_bill=0
        for i in range(len(quantity_list)):
            total_bill+=quantity_list[i]*price_list[i]
        self.__bill_amount=consultation_fees+total_bill

bill=Bill("Bill_101","Shweta Julur")
bill.calculate_bill_amount(200,[4,3,2,1],[100,200,300,200])
print(bill.get_bill_id())
print(bill.get_patient_name())
print(bill.get_bill_amount())