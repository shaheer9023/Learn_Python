'''Write a program to print the following star pattern.
  *
 ***
***** for n = 3'''
lines=int(input("enter number of lines"))
for i in range(1,lines+1):
    print(" "*(lines-i),end="")
    print("*"*(2*i-1),end="")
    print("")