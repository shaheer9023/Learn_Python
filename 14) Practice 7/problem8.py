'''Write a program to print the following star pattern: 
*
**
*** for n = 3'''

lines = int(input("enter number of stars : "))
for i in range(1, lines+1):
    print("*"*i)
    i = i+1
