# functions in string 
name="shaheer"

print(len(name))#length starts from 1 so output is 7

# ye btata h k aap ki string ka given end true h ya false 
print(name.endswith("er"))#true
print(name.endswith("r"))#true
print(name.endswith("el"))#false
print(name.endswith("l"))#false

# similarly start ki value 
print(name.startswith("sh"))#true

# ye fucntion string k first letter ko capital krta 
print(name.capitalize())#Shaheer

# ye poori string capital krta 

print(name.upper())#SHAHEER

# poori string small
print(name.lower())#shaheer

# hr word ka first letter capital
fullname="shaheer ahmad"
print(fullname.title())#Shaheer Ahmad

# find index
array="123456"
print(array.find("5"))

# replace 
print(fullname.replace("shaheer","Anas"))#Anas ahmad