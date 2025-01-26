'''1.
 Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
'''
with open("poem.txt") as file:
    content=file.read()
    if("twinkle" in content):
        print(" twinkle is present ")
    else:
        print("twinkle is not present ")
