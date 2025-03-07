"""1. Create a class (2-D vector) and use it to create another class representing a 3-D vector."""
class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    @property
    def show(self):
        print(f"the sum of 2D vector is {self.i}i + {self.j}j")    
    
class threeDvector(twoDvector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    @property
    def show(self):
        print(f"the sum of 3D vector is {self.i}i + {self.j}j + {self.k}k")    
t2=twoDvector(23,6)
print("-"*50)
t2.show
t3=threeDvector(33,45,66)
print("-"*50)
t3.show
print("-"*50)
        
            

    
        