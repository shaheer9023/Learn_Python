# """The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score."""
import random
def game():
    print("you are playing game .... ")
    
    score = random.randint(1,20)
    # fetch Hi-score form file
    with open("hiScore.txt") as file:
        highscore=file.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0
    print(f"high score is {score}")
    if(score>highscore):
            # now update file 
            with open("hiScore.txt","w") as file:
                 file.write(str(score))

                 return score
game()
            


