"""
Create a class “Programmer” for storing information of few programmers working at Microsoft.
"""
class programmer:
    companay="MicroSoft"
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id

shaheer=programmer("Shaheer",100000,313)        
Ahmad=programmer("Ahmad",200000,314)        
shoaib=programmer("Shoaib",300000,314)        
print(shaheer.name,shaheer.companay,shaheer.salary,shaheer.id)
print(Ahmad.name,Ahmad.companay,Ahmad.salary,Ahmad.id)
print(shoaib.name,shoaib.companay,shoaib.salary,shoaib.id)