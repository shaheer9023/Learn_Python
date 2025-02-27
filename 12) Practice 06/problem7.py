# Write a program to find out whether a given post is talking about “shaheer” or not.

post=input("enter post : ")
if("shaheer".lower() in post.lower()):
    print("yes shaheer is talking in post")
else:
    print("no shaheer is not talking in post")