#OOPR-Assgn-11
flowers={"orchid":15,"rose":25,"jasmine":40}

class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
    
    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name
        
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg
        
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available
        
    def get_flower_name(self):
        return self.__flower_name
        
    def get_price_per_kg(self):
        return self.__price_per_kg
        
    def get_stock_available(self):
        return self.__stock_available
        
    def validate_flower(self):
        if self.get_flower_name().lower() in flowers.keys():
            return True
        else:
            return False
    
    def validate_stock(self,required_quantity):
        if required_quantity<=self.get_stock_available():
            return True
        else:
            return False
    
    def sell_flower(self,required_quantity):
        if self.validate_flower():
            if self.validate_stock(required_quantity):
                self.set_stock_available(self.get_stock_available()-required_quantity)
    
    def check_level(self):
        if self.validate_flower():
            if self.get_stock_available()<flowers[self.get_flower_name().lower()]:
                return True
            else:
                return False
        else:
            return False