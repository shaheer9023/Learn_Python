'''
4.
A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
'''
word="Donkey"
with open("file.txt","r") as file:
    content=file.read()


    newcontent=content.replace(word,"######")
    with open("file.txt","w") as file:
        file.write(newcontent)
