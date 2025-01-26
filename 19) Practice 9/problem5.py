'''
5.
Repeat program 4 for a list of such words to be censored.
'''
words=["tota","main"]
with open("file2.txt","r") as file:
    content=file.read()
for word in words:
    content=content.replace(word,"#"*len(word))

with open("file2.txt","w") as file:
    file.write(content)