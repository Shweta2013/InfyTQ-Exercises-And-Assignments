#DSA-Assgn-12
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if self.__top==self.get_max_size()-1:
            return True
        else:
            return False
            

    def push(self,data):
        if self.is_full() is False:
            self.__top+=1
            self.__elements.insert(self.__top,data)
        else:
            print("Stack is full")

    
    def is_empty(self):
        if self.__top==-1:
             return True
        else:
            return False
    
    def pop(self):
        if self.is_empty() is False:
            value=self.__elements[self.__top]
            self.__top-=1
            return value
        else:
            print("Stack is empty")

    def display(self):
        top=self.get_top()
        while(top!=self.get_max_size() and top!=-1):
            print(self.__elements[top],end=" ")
            top-=1

class Ball:
    def __init__(self,color,name):
        self.__color=color
        self.__name=name
        
    def __str__(self):
        return (self.__color+" "+self.__name)
    
    def get_color(self):
        return self.__color
    
    def get_name(self):
        return self.__name
             
class Game:
    ball_container=[]
    red_balls_container=[]
    green_balls_container=[]
    blue_balls_container=[]
    yellow_balls_container=[]
    def __init__(self,ball_stack):
        self.ball_container=ball_stack
        self.red_balls_container=None
        self.green_balls_container=None
        self.blue_balls_container=None
        self.yellow_balls_container=None
    
    def grouping_based_on_color(self):
        for ball in self.ball_container:
            if ball.get_color()==Red:
                red_balls_container.append(ball)
                
            if ball.get_color()==Blue:
                blue_balls_container.append(ball)
                
            if ball.get_color()==Green:
                green_balls_container.append(ball)
                
            if ball.get_color()==Yellow:
                yellow_balls_container.append(ball)
        return red_balls_container
        # print(green_balls_container)
        # print(blue_balls_container)
        # print(yellow_balls_container)
    def rearrange_balls(self,color):
        pass
    def display_ball_details(self,color):
        pass
    
#Use different values to test your program
ball1=Ball("Red","A")
ball2=Ball("Blue","B")
ball3=Ball("Yellow","B")
ball4=Ball("Blue","A")
ball5=Ball("Yellow","A")
ball6=Ball("Green","B")
ball7=Ball("Green","A")
ball8=Ball("Red","B")
ball_list=Stack(8)
ball_list.push(ball1)  
ball_list.push(ball2) 
ball_list.push(ball3) 
ball_list.push(ball4) 
ball_list.push(ball5) 
ball_list.push(ball6) 
ball_list.push(ball7) 
ball_list.push(ball8)   

game=Game(ball_list)
print(game.grouping_based_on_color())


#Create objects of Game class, invoke the methods and test the program