# Check the type of variable assigned using input () function.
variable=input("enter any variable : ")
print("type of variale is : ",type(variable))#here type is class <str>
# but as we know default input value is string , if you don't know check README file of variable and datatypes

# we can use type conversion
variable2=int(variable)
print("after type conversion the above type is changed to : ",type(variable2))# class<int>