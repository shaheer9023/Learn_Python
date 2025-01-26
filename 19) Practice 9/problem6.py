'''
6.
Write a program to mine a log file and find out whether it contains ‘python’.
'''
with open("log.txt","r") as file:
    content=file.read()
if "python" in content:
    print("yes python is present ")
else:
    print("no python is not present ")