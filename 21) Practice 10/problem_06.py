"""
Can you change the self-parameter inside a class to something else.Try changing self to “slf”and see the effects.
"""


from random import randint
class Train:
   
    def __init__(sel):
        sel.trainNo=None
        sel.fro=None
        sel.to=None
        
    def book(sel):
        print("*********WELCOME TO PAKISTAN RAILWAYS***********")
        print("please enter Booking Details ")
        sel.trainNo=int(input("enter train number : "))
        sel.fro=input("from : ")    
        sel.to=input("TO : ")
    def status(sel):
        if sel.trainNo is not None:
         print(f"STATUS: your train with train number {sel.trainNo} from {sel.fro} to {sel.to} is Booked Successfully")
        else:
           print("No Booking Found ")
 
    def fare(sel):
        if sel.trainNo is not None:
         print(f" FARE: your  fare  of booked ticket from {sel.fro} to {sel.to} is {randint(1000,2000)} PKR. ")
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


#   YES WE CAN CHANGE SELF TO ANYTHING ELSE
