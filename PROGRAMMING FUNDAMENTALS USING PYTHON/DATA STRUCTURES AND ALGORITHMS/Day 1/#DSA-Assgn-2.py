#DSA-Assgn-2
import operator

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

#Implement Service class here
class Service(Car):
    def __init__(self,car_list):
        self.__car_list=car_list
        
    def get_car_list(self):
        return self.__car_list
            
    def find_cars_by_year(self,year):
        car_list_by_year=[]
        for i in self.__car_list:
            if i.get_year()==year:
                car_list_by_year.append(i.get_model())
        if len(car_list_by_year)==0:
            return None
        return car_list_by_year
        
    def add_cars(self,new_car_list):
        self.__car_list.extend(new_car_list)
        self.__car_list.sort(key=lambda x: x.get_year())
    
    def remove_cars_from_karnataka(self):
        state_to_be_removed="KA"
        car_list_copy=self.__car_list.copy()
        for car in car_list_copy:
            if (car.get_registration_number()).startswith("KA"):
                self.__car_list.remove(car)
        
        
car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
car6=Car("City Honda",2015,"TS07 4331")
car7=Car("Jaguar",2014,"MH07 433232")
car8=Car("Scala",2012,"MH07 4312")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
car_list1=[car6,car7,car8]

service1=Service(car_list)
print(service1.find_cars_by_year(2013))

print(service1.add_cars(car_list1))
print(service1.get_car_list())

service1.remove_cars_from_karnataka()
print(service1.get_car_list())
#Create object of Service class, invoke the methods and test your program