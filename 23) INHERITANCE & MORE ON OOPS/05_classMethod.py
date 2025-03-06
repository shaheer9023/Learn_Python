class number:
    num=5
    def show(cls):
        print(f"value of class attribute num = {cls.num}")
n=number()
n.num=50
n.show()   # OUTPUT: number of class attribute num = 50 because self parameter shows instance value 
"""for class attribute value we use @classmethod"""
class number:
    num=5
    @classmethod
    def show(cls):
        print(f"value of class attribute num = {cls.num}")
n=number()
n.num=50
n.show() # OUTPUT: number of class attribute num = 5