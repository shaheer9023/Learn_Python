# Write a program to print multiplication table of n using for loops in reversed order.

number=int(input("enter number of table : "))
print(f"table of {number} in reverse order : ")

for i in range (1,11):
    print(f"{number} X {11-i} = {number*(11-i)}")
    i=i+1