"""Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’."""
class Animals:
    pass
class pets(Animals):
    pass
class Dogs(pets):
    @staticmethod
    def bark():
        print("BOW BOW!!")
d=Dogs()
d.bark()


