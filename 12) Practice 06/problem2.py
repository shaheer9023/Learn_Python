'''Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.'''

marks1=int(input("enter marks 1 : "))
marks2=int(input("enter marks 2 : "))
marks3=int(input("enter marks 3 : "))

if(marks1>100 and marks2>100 and marks3>100):
    print("you entered invalid marks plz enter less than or equal to 100")


total_percentage=(100*(marks1+marks2+marks3)/300)
subj1_percentage=(100*(marks1)/100)
subj2_percentage=(100*(marks2)/100)
subj3_percentage=(100*(marks3)/100)
if(total_percentage>=40):
    print("you are overall pass and your overall percentage is ",total_percentage,"%")
else:
    print("you are fail by obtaining ",total_percentage,"%")

if(subj1_percentage<33):
    print("yor are fail in subject 1 by obtainong ",subj1_percentage,"%")    
if(subj2_percentage<33):
    print("yor are fail in subject 2 by obtainong ",subj2_percentage,"%")    
if(subj3_percentage<33):
    print("yor are fail in subject 3 by obtainong ",subj3_percentage,"%")    