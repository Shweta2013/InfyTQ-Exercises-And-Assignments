class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    
    def get_vehicle_id(self):
        return self.__vehicle_id
    
    def get_vehicle_type(self):
        return self.__vehicle_type
    
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    
    def get_premium_amount(self):
        return self.__premium_amount
    
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
    
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    
    def calculate_premium(self):
        if self.get_vehicle_type()=="Two Wheeler":
            amount=self.get_vehicle_cost()*0.02
            self.set_premium_amount(amount)
        elif self.get_vehicle_type()=="Four Wheeler": 
            amount=self.get_vehicle_cost()*0.06
            self.set_premium_amount(amount)
        else:
            print("Invalid vehicle type")
    def display_vehicle_details(self):
        print(self.get_vehicle_id()+" "+self.get_vehicle_type()+" "+self.get_vehicle_cost()+" "+self.get_premium_amount())

vehicle1=Vehicle()