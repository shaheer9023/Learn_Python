"""
Add a static method in problem 2, to greet the user with hello.
"""
class calculator:
    def __init__(self,num):
        self.num=num
   
    def square(self):
        print(f"square of given number is {self.num*self.num}")
    def cube(self):
        print(f"cube of given number is {self.num*self.num*self.num}")
    def squrt(self):
        print(f"square root of given number is {self.num**1/2}")
    @staticmethod    
    def hello():
        print("Hello this is class named calculator ")

number=int(input("enter number : "))
c=calculator(number)
c.hello()
c.square()
c.cube()
c.squrt()