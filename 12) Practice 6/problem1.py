# Write a program to find the greatest of four numbers entered by the user.
number1=int(input("Enter number 1 : "))
number2=int(input("Enter number 2 : "))
number3=int(input("Enter number 3 : "))
number4=int(input("Enter number 4 : "))
if(number1>number2 and number1>number3 and number1>number4 ):
    print("number 1 is greater ")
elif(number2>number1 and number2>number3 and number2>number4 ):
    print("number 2 is greater ")
elif(number3>number1 and number3>number2 and number3>number4 ):
    print("number 3 is greater ")
else:
    print("number 4 is greater ")