""" without length argument"""
def Sum(num1,num2):
    total=num1+num2
    print(total)

Sum(10,3) 
# Sum(10,20,30,40) # error aayga q k humny bs 2 parameters diye hain or yahan hum 4 arguments paSS Kr rhy 

"""with lenghts Argument"""
def Sum(*numbers): # iska syntax ye h k parameter k sath * lgta h 
    total=sum(numbers)
    print(total)
Sum(10,20,30)    # jitny mrzi arguments pass krty jao add hota jaygaa

"""keywords Arguments"""
def information(**details):
    print(f"details are {details}")
    for key,value  in details.items():

     print(f"{key} : {value}  ")

information(name="shaheer",age=21,language="python",ID=313)    

"""both length and keyword arguments"""
def employee(language,*name,**department):
    print(f"language is : {language}")
    print(f"names are : {name}")
    print(f"departments are : {department}")
    for names in name:
        print(f"name : {names}")

    for dept,field  in department.items():
        print(f"department = {dept} : filed = {field}")   
employee("python","anas","shaheer","ahmad",Master="Ai",ADP="CS")    
    
