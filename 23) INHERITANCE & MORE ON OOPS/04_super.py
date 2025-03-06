class parent:
  def __init__(self):
    super().__init__()
    print("i am constructor of parent")
class child1(parent):
  def __init__(self):
    super().__init__()
    print("i am constructor of child 1")
class child2(child1):
  def __init__(self):
    super().__init__()
    print("i am constructor of child 2")
   
c=child2()
