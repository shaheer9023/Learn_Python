
class employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property # this is getter method actually    
    def mail(self):    
        return f"{self.first}{self.last}@gmail,com"
    @mail.deleter
    def mail(self):
         
        self.first=None
        self.last=None   
      

print("-"*50)
e2=employee("Anas","Ahmad")
print(e2.first)
print("-"*50)
e2.last="Shaheer"
print(e2.last)
print("-"*50)
del e2. mail
print(e2.mail) 
print("-"*50)