#OOPR-Assgn-19
#OOPR-Exer-7

class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None
        
    def validate_source_destination(self):
        s=self.get_source().lower()
        d=self.get_destination().lower()
        if s=="delhi":
            if d=="mumbai" or d=="pune" or d=="chennai" or d=="kolkata":
                return True
            else:
                return False
        else:
            return False
    
    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter+=1
            s=self.get_source()
            d=self.get_destination()
            if Ticket.counter<10:
                self.__ticket_id=s[0].upper()+d[0].upper()+str(0)+str(Ticket.counter)
            else:
                self.__ticket_id=s[0].upper()+d[0].upper()+str(Ticket.counter)
        else:
            self.__ticket_id=None
    
    def get_ticket_id(self):
        return self.__ticket_id
    
    def get_passenger_name(self):
        return self.__passenger_name
    
    def get_source(self):
        return self.__source
    
    def get_destination(self):
        return self.__destination
        
ticket=Ticket("Shweta","Delhi","Kolkata")
ticket.generate_ticket()
print(ticket.get_passenger_name())
print(ticket.get_source())
print(ticket.get_destination())
print(ticket.get_ticket_id())