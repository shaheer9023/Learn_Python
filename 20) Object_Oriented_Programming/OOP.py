""" classes"""
# class employee:
#    name="shaheer"
#    salary=1200000
# shaheer=employee()
# print(shaheer.name,shaheer.salary) OutPUT = shaheer 313

"""Class Vs Instance Attributes"""
# class employee:
#    name="shaheer"  name and salary are class attributes 
#    salary=1200000
# shaheer=employee()
# shaheer.name="Anas" # shaheer.name is object or instance attribute
# print(shaheer.name,shaheer.salary) output = Anas 313 
# Note : Instance attribute take preference over class attribute  

"""Self Argument"""
# class employee:
#    name="shaheer"
#    salary=1200000
#    def getInfo(self):
#     print(f"my name is {self.name} and my salary is {self.salary}")
# shaheer=employee()
# shaheer.getInfo()
# print(shaheer.name,shaheer.salary) 

"""Static Method"""
# class employee:
#    name="shaheer"
#    salary=1200000
#    """if you dont want to give self argument than use key static method"""
#    @staticmethod
#    def getInfo():
#     print(f"my name is {employee.name} and my salary is {employee.salary}")
# shaheer=employee()
# shaheer.getInfo()
# print(shaheer.name,shaheer.salary) 

"""Init Constructor()"""
"""contructor is a function which calls automatically when programme runs """
class hello():
    greet="Hello!  Good Morning "
    def __init__(self):
        print("i am constructor and i am running automatically ")
Greet=hello()
print(Greet.greet)      

