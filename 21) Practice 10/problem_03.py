"""
Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
"""


class sample:
    """suppose """
    a = 5  # here a is class attribute


s = sample()

print(s.a)  # output is 5 because still programme having no instance attribute
"""now make instance attribute with same name """
s.a = 10
# now output is 10 because instance attribute take preference over class attribute
print(s.a)
"""now check did it change value of class attribute ?? """
print(sample.a)  # output is 5 means class attribute will not change
