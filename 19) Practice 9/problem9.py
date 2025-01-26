'''
9.
Write a program to find out whether a file is identical & matches the content of another file.
'''
# we have to make 2 files 
with open("this.txt")as file:
    content1=file.read()
with open("copy_this.txt")as file:
    content2=file.read()
if(content1==content2):
    print("both files are identical ")
else:
    print("not identical")
