
# 1. Write a program using functions to find greatest of three numbers.
def greatest():
    one=int(input("enter 1st number : "))
    second=int(input("enter second number : "))
    third=int(input("enter third number : "))
    if(one>second and one>third):
        print(f"{one} is greatest ")
    elif(second>one and second>third):
        print(f"{second} is greatest ")
    else:
        print(f"{third} is greatest ")

greatest()