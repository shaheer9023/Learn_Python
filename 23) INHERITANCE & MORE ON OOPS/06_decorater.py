"""Here greet is decorator"""
def greet(hello):
    def salam():
        print("Assalam o Alaikum")
        hello()
        print("JazakAllah")
    return salam
@greet    
def hello():
    print("My name is Shaheer")
hello()
print("-"*50)
"""example"""
def intro(name):
    def salam():
        print("👋 Salam!")
        name()
        print("👋 Allah Hafiz!")
    return salam
@intro
def say_name():
    print("Mera naam Shaheer hai.")
say_name() 
print("-"*50)
'''complex example'''
def multiply(add):
    def combine(a,b):
        print(f"{add(a,b)*2}")
    return combine
@multiply    
def add(a,b):
    return a+b

print("the addition of a and b with multiply by 2 is = ")
add(5,2)

print("-"*50)
"""example"""
def func(num):
    def square():
        value = num()
        print(f"square of {value} is {value * value}")
        return value * value  # Return kar raha hai
    return square


@func    
def num():
    return 5

# Ab return value ko store kar ke print bhi kar rahe hain
result = num()
print(f"Returned value: {result}")


