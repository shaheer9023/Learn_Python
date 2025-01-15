# # snake , water , gun game 
# '''
# 1 for snake
# 2 for water
# 3 for gun
# '''
import random
computer=random.choice([1,2,3])
yourInput = input("Enter your choice (snake, water, gun): ")
computerDictionary={1:"snake",
            2:"water",
            3:"gun"}
yourDictionary={"snake":1,
                "water":2,
                "gun":3}
# apny string ko integer me convert krny k liye 
if yourInput in yourDictionary:# check krygaa k apka input aap ki dictionary me h k ni  
    you = yourDictionary[yourInput] # ye line apki string ko apki dictionary k integer se replace kr degi 
print(f"computer choose = {computerDictionary[computer]}\n you choose = {yourInput} ")
if(computer==you):
    print("====RESULT====")
    print("its Draw 🆗")
else:
    if(computer==1 and you==2):
        print("Snake drinks the water hence YOU LOSE 💔.")
    elif(computer==2 and you==1):
        print("Snake drinks the water hence YOU WIN 💖.")
    elif(computer==1 and you==3):
        print("Gun will kill the snake and YOU WIN 💖.")
    elif(computer==3 and you==1):
        print("Gun will kill the snake and YOU LOSE 💔.")
    elif(computer==3 and you==2):
        print("The gun will drown in water,YOU WIN 💖.")
    elif(computer==2 and you==3):
        print("The gun will drown in water,YOU LOSE 💔.")


    else:
     print("Something went wrong...")



