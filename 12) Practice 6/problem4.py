'''Write a program to find whether a given username contains less than 10 characters or not.'''
username=input("enter username : ")
if(len(username)>10):
    print(f"username contain character more than 10 characters i.e {len(username)}")
else:
    print(f"username has less than 10 characters i.e {len(username)}")