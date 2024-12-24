# Practice # 6 Explanation

### 1. **Greatest of Four Numbers**

#### Code:
```python
# User inputs the first number
number1 = int(input("Enter number 1 : "))
# User inputs the second number
number2 = int(input("Enter number 2 : "))
# User inputs the third number
number3 = int(input("Enter number 3 : "))
# User inputs the fourth number
number4 = int(input("Enter number 4 : "))
# Check if number1 is the greatest
if(number1 > number2 and number1 > number3 and number1 > number4):
    print("number 1 is greater ")
# Check if number2 is the greatest
elif(number2 > number1 and number2 > number3 and number2 > number4):
    print("number 2 is greater ")
# Check if number3 is the greatest
elif(number3 > number1 and number3 > number2 and number3 > number4):
    print("number 3 is greater ")
# If none of the above conditions are true, number4 is the greatest
else:
    print("number 4 is greater ")
```



**Example 1:**
```
Enter number 1 : 20
Enter number 2 : 35
Enter number 3 : 50
Enter number 4 : 25
Output: number 3 is greater
```

**Example 2:**
```
Enter number 1 : 40
Enter number 2 : 30
Enter number 3 : 25
Enter number 4 : 45
Output: number 4 is greater
```

### 2. **Student Pass/Fail Check (based on marks)**

#### Code:
```python
# User inputs marks for the first subject
marks1 = int(input("enter marks 1 : "))
# User inputs marks for the second subject
marks2 = int(input("enter marks 2 : "))
# User inputs marks for the third subject
marks3 = int(input("enter marks 3 : "))

# Check if any marks are greater than 100, which is invalid
if(marks1 > 100 and marks2 > 100 and marks3 > 100):
    print("you entered invalid marks plz enter less than or equal to 100")

# Calculate total percentage for all subjects
total_percentage = (100 * (marks1 + marks2 + marks3) / 300)
# Calculate percentage for the first subject
subj1_percentage = (100 * (marks1) / 100)
# Calculate percentage for the second subject
subj2_percentage = (100 * (marks2) / 100)
# Calculate percentage for the third subject
subj3_percentage = (100 * (marks3) / 100)
# Check if the overall percentage is 40% or higher
if(total_percentage >= 40):
    print("you are overall pass and your overall percentage is ", total_percentage, "%")
else:
    print("you are fail by obtaining ", total_percentage, "%")

# Check if the student failed in subject 1
if(subj1_percentage < 33):
    print("yor are fail in subject 1 by obtaining ", subj1_percentage, "%")    
# Check if the student failed in subject 2
if(subj2_percentage < 33):
    print("yor are fail in subject 2 by obtaining ", subj2_percentage, "%")    
# Check if the student failed in subject 3
if(subj3_percentage < 33):
    print("yor are fail in subject 3 by obtaining ", subj3_percentage, "%")    
```



**Example 1:**
```
enter marks 1 : 40
enter marks 2 : 50
enter marks 3 : 70
Output: you are overall pass and your overall percentage is  53.33 %
```

**Example 2:**
```
enter marks 1 : 30
enter marks 2 : 20
enter marks 3 : 40
Output: you are fail by obtaining  30.0 %
```

### 3. **Spam Comment Detector**

#### Code:
```python
# Define spam keywords
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

# User inputs a message
message = input("enter a comment : ")
# Check if the message contains any spam keywords
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this message is a spam")
# If no spam keywords are found
else:
    print("this message is not a spam ")    
```


**Example 1:**
```
enter a comment : Buy now to get great discounts!
Output: this message is a spam
```

**Example 2:**
```
enter a comment : How are you doing today?
Output: this message is not a spam
```

### 4. **Username Length Check**

#### Code:
```python
# User inputs a username
username = input("enter username : ")
# Check if the username has more than 10 characters
if(len(username) > 10):
    print(f"username contain character more than 10 characters i.e {len(username)}")
# If the username has 10 or fewer characters
else:
    print(f"username has less than 10 characters i.e {len(username)}")
```



**Example 1:**
```
enter username : myuser12345
Output: username contain character more than 10 characters i.e 12
```

**Example 2:**
```
enter username : shaheer
Output: username has less than 10 characters i.e 7
```

### 5. **Name Search in List**

#### Code:
```python
# Define a list of names
list = ["shaheer", "fatima", "anas", "ahmad", "muzammil",]
# User inputs a name
name = input("enter name : ")
# Check if the name is in the list
if(name in list):
    print("yes name is present in list ")
# If the name is not in the list
else:
    print("oopss name not found...")
```


**Example 1:**
```
enter name : shaheer
Output: yes name is present in list
```

**Example 2:**
```
enter name : ahmed
Output: oopss name not found...
```

### 6. **Grade Calculation Based on Marks**

#### Code:
```python
# User inputs marks
marks = int(input("enter your marks : "))
# Check if the marks are invalid (greater than 100 or less than 0)
if(marks > 100 or marks < 0):
        print("you entered invalid marks")

# Determine the grade based on marks
if(marks >= 90 and marks <= 100):
    print("your grade is Ex")
elif(marks >= 80 and marks < 90):
     print("your grade is A")
elif(marks >= 70 and marks < 80):
    print("your grade is B")
elif(marks >= 60 and marks < 70):
    print("your grade is C")
elif(marks >= 50 and marks < 60):
    print("your grade is D")
elif(marks < 50):
    print("your grade is F")
```



**Example 1:**
```
enter your marks : 95
Output: your grade is Ex
```

**Example 2:**
```
enter your marks : 45
Output: your grade is F
```

### 7. **Post Contains "shaheer"**



#### Code:
```python
# User inputs a post
post = input("enter post : ")
# Check if "shaheer" is mentioned in the post
if("shaheer".lower() in post.lower()):
    print("yes shaheer is talking in post")
# If "shaheer" is not mentioned
else:
    print("no shaheer is not talking in post")
```

---

#### Example 1 (Jab "shaheer" mention ho post mein):
```
enter post : Shaheer is a great developer!
Output: yes shaheer is talking in post
```

#### Example 2 (Jab "shaheer" mention na ho post mein):
```
enter post : Fatima is working on her project.
Output: no shaheer is not talking in post
```

---

### Explanation:
- Code post input karta hai aur case-insensitive tarike se "shaheer" ko dhoondta hai. 
- Agar "shaheer" post mein hai, toh message print hota hai: **"yes shaheer is talking in post"**.
- Agar nahi hai, toh message print hota hai: **"no shaheer is not talking in post"**.