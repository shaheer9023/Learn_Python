class book:
    def __init__(self,title,pages):
             self.title=title
             self.pages=pages
    def __add__(self,other):
           return book("combined book",self.pages + other.pages)
                    
b1=book("learn python",300)
b2=book("learn C++",500)
b3=book("learn typescript",300)
b4=book("learn typescript",300)
b5=book("learn typescript",300)
b6=book("learn typescript",300)

result=b1+b2+b3+b4+b5+b6
print(f"total pages are {result.pages}")