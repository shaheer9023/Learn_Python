'''
8.
Write a program to make a copy of a text file “this. txt”

'''
with open("this.txt") as file:
    content=file.read()

    with open("copy_this.txt","w") as file:
     file.write(content)
