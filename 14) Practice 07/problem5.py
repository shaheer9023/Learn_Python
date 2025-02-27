# Write a program to find the sum of first n natural numbers using while loop.
number=int(input("enter number : "))
i=1 # because natural number starts from 1 
sum=0
while(i<=number):
    sum=sum+i
    i=i+1

print("total sum is ",sum)