class employee:
    def name(self):
     self.name=input("enter your name : ")
     print(f"my name is {self.name}")

class manager:
        def information(self):
         self.companay="Microsoft"
         print(f"my name is {self.name} and i am manager of {self.companay}")
"""here CEO class contains All Attributes of employee class and manager class"""
class CEO(employee,manager):
    def CEO(self):
        print(f"i am CEO in {self.companay}")

e=employee()
e.name()
# e.information() shows error because employee class has no information attribute / function

c=CEO()
c.name()
c.information()
c.CEO()        