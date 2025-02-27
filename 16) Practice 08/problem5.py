'''
5.
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''
def stars():
    n=int(input("enter number of stars : "))
    for i in range(n,0,-1):
        print("*"*i)
stars()        