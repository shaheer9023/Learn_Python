"""Simple Class """
class employee:
    def name(self):
     self.name=input("enter your name : ")
     print(f"my name is {self.name}")
e=employee()
e.name()        

"""Single Inheritance """
class employee:
    def name(self):
     self.name=input("enter your name : ")
     print(f"my name is {self.name}")

"""manager class contain all attributes of employee class """

class manager(employee):
        
        def information(self):
         self.companay="Microsoft"
         print(f"my name is {self.name} and i am manager of {self.companay}")

object=manager()

object.name()
object.information()