class employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.mail=f"{self.first}{self.last}@gmail,com"

"""ye to ho gaya seedha seedha"""

e1=employee("shaheer","ahmad")
print(e1.first)
print("-"*50)
print(e1.last)
print("-"*50)
print(e1.mail)
print("-"*50)

print("""now change value of  instance attribute""")
print("-"*50)
e2=employee("Anas","Ahmad")
print(e2.first)
print("-"*50)
e2.last="Shaheer"
print(e2.last)
print("-"*50)
print(e2.mail)# email still remain same 
print("-"*50)


print("Now make email as function to solve this ")
class employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def mail(self):    
        return f"{self.first}{self.last}@gmail,com"

print("-"*50)
e2=employee("Anas","Ahmad")
print(e2.first)
print("-"*50)
e2.last="Shaheer"
print(e2.last)
print("-"*50)
print(e2.mail()) # msla to slove ho gaya h but ab msla ye h k mujhe mail function call krna pr raha h but me chahta hoon k me object print krun
print("-"*50)

print("now we use property decorator to solve this ")

class employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property # simply add this     
    def mail(self):    
        return f"{self.first}{self.last}@gmail,com"

print("-"*50)
e2=employee("Anas","Ahmad")
print(e2.first)
print("-"*50)
e2.last="Shaheer"
print(e2.last)
print("-"*50)
print(e2.mail) # our issue is resolved
print("-"*50)