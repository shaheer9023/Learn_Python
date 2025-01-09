"""Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Shaheer", "Soban", "Anas", "Ahmad"]"""

list = ["Shaheer", "Soban", "anas", "Ahmad"]
for name in list:
    if(name.startswith("S") ):
        print(f"Hello {name}")