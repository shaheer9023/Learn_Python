# Write a program to print multiplication table of a given number using for loop.

number=int(input("enter number of table : "))
print(f"table of {number}  : ")
for i in range (0,11):
    print(f"{number} X {i} = {i*number}")
    i=i+1