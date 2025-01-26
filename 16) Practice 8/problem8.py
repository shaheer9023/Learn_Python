# 8.  Write a python function to print multiplication table of a given number.
def table():
    number=int(input("Enter number "))
    for i in range(0,11):
        print(f"{number} x {i} = {i*number} ")
table()        