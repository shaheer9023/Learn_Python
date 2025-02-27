'''
3.
Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
'''
def generateTable(n):
    table = f"Multiplication Table of {n}\n"
    for i in range(0,11):
        table+=f"{n} X {i} = {i*n}\n"
    with open(f"tables/table_{n}.txt","w") as file:
        file.write(table)
for i in range(2,21):
    generateTable(i)
        


