'''
7.
Write a program to find out the line number where python is present from ques 6.
'''
with open("log.txt") as file:
    for lineNumber,lineContent in enumerate(file,start=1):
        if("python" in lineContent.lower()):
            print(f"python present in line :{lineNumber} ")
        

