"""
Write a class “Calculator” capable of finding square, cube and square root of a number.
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
number=int(input("enter number : "))
c=calculator(number)
c.square()
c.cube()
c.squrt()
