"""Write a Class ‘Train’ which has methods to book a ticket, get status  and get fare information of train running under Pakistan Railways."""
from random import randint
class Train:
   
    def __init__(self):
        self.trainNo=None
        self.fro=None
        self.to=None
        
    def book(self):
        print("*********WELCOME TO PAKISTAN RAILWAYS***********")
        print("please enter Booking Details ")
        self.trainNo=int(input("enter train number : "))
        self.fro=input("from : ")    
        self.to=input("TO : ")
    def status(self):
        if self.trainNo is not None:
         print(f"STATUS: your train with train number {self.trainNo} from {self.fro} to {self.to} is Booked Successfully")
        else:
           print("No Booking Found ")
 
    def fare(self):
        if self.trainNo is not None:
         print(f" FARE: your  fare  of booked ticket from {self.fro} to {self.to} is {randint(1000,2000)} PKR. ")
        else:
         print("No Booking Found ")    


# Object create karna
ticket = Train()  

# Booking karna
ticket.book()

# Booking status check karna
ticket.status()

# Fare check karna
ticket.fare()

