
class employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property # this is getter method actually    
    def mail(self):    
        return f"{self.first}{self.last}@gmail,com"
    @mail.setter
    def mail(self,mail):
        first,last=mail.split() 
        self.first=first
        self.last=last   
      

print("-"*50)
e2=employee("Anas","Ahmad")
print(e2.first)
print("-"*50)
e2.last="Shaheer"
print(e2.last)
print("-"*50)
e2.mail="shaheer ahmad9023"
print(e2.mail) 
print("-"*50)