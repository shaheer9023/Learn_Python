class parent1:
    a=1
class parent2(parent1):
    b=2
class child(parent2):
    c=3 
p1=parent1()
p2=parent2()
c=child()
print(p1.a) # 1
# print(p1.b) error
print(p2.a) # 1
print(p2.b) # 2
# print(p2.c) error
print(c.a) # 1
print(c.b) # 2
print(c.c) # 3
