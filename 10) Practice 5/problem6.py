# problem 6
'''Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.'''
dict={}
name=input("enter friends name : ")
language=input("enter language : ")
dict.update({name:language})
name=input("enter friends name : ")
language=input("enter language : ")
dict.update({name:language})
name=input("enter friends name : ")
language=input("enter language : ")
dict.update({name:language})
name=input("enter friends name : ")
language=input("enter language : ")
dict.update({name:language})
print(dict)