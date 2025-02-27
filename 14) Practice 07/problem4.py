# Write a program to find whether a given number is prime or not.
number=int(input("enter number : "))

for i in range(2,number):
    if(number%i==0):
        print(f"{number} is not a prime number.")
        break
else:
    print(f"{number} is a prime number. ")



