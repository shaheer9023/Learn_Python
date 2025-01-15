# Explanation Project # 1
```python
# Snake, Water, Gun Game
# '''
# 1 for snake
# 2 for water
# 3 for gun
# '''
import random  # Random module ko import kar rahe hain random choices ke liye

# Computer randomly apni choice karega (1 = snake, 2 = water, 3 = gun)
computer = random.choice([1, 2, 3])

# User input lega aur snake, water ya gun enter karne ko kahega
yourInput = input("Enter your choice (snake, water, gun): ")

# Computer ke choices ko define kar rahe hain (mapping integer to string)
computerDictionary = {1: "snake", 2: "water", 3: "gun"}

# User ke choices ko define kar rahe hain (mapping string to integer)
yourDictionary = {"snake": 1, "water": 2, "gun": 3}

# Input validate karenge: agar user ka input dictionary ke andar hai toh
if yourInput in yourDictionary:  # Ye check karega ke user ka input sahi hai ya nahi
    you = yourDictionary[yourInput]  # String input ko uske corresponding integer me convert karenge

# Computer aur user ki choices ko print karenge
print(f"Computer chose = {computerDictionary[computer]}\nYou chose = {yourInput}")

# Game ka result check karenge
if computer == you:  # Agar computer aur user ki choice same hai, toh draw hoga
    print("====RESULT====")
    print("It's a Draw 🆗")
else:
    # Agar choices alag hain, toh har case ke liye alag result check karenge
    if computer == 1 and you == 2:  # Snake vs Water
        print("Snake drinks the water hence YOU LOSE 💔.")
    elif computer == 2 and you == 1:  # Water vs Snake
        print("Snake drinks the water hence YOU WIN 💖.")
    elif computer == 1 and you == 3:  # Snake vs Gun
        print("Gun will kill the snake and YOU WIN 💖.")
    elif computer == 3 and you == 1:  # Gun vs Snake
        print("Gun will kill the snake and YOU LOSE 💔.")
    elif computer == 3 and you == 2:  # Gun vs Water
        print("The gun will drown in water, YOU WIN 💖.")
    elif computer == 2 and you == 3:  # Water vs Gun
        print("The gun will drown in water, YOU LOSE 💔.")
    else:
        print("Something went wrong...")  # Agar koi unexpected condition ho
```

---

### Example Input and Output:

#### **Input**:
```
Enter your choice (snake, water, gun): gun
```

#### **Output**:
```
Computer chose = snake
You chose = gun
Gun will kill the snake and YOU WIN 💖.
```

---

### Comments in Code:

1. **`import random`**:
   - Random choices ke liye Python ka built-in module import kiya.

2. **`computer = random.choice([1, 2, 3])`**:
   - Computer randomly ek integer select karega (1, 2, ya 3).

3. **`yourInput = input(...)`**:
   - User se input liya (snake, water, ya gun).

4. **Validation with `if yourInput in yourDictionary`**:
   - Check karta hai ke user ka input valid hai ya nahi.

5. **Dictionaries**:
   - `computerDictionary` ka use computer ki choice ko string me convert karne ke liye hota hai.
   - `yourDictionary` user ke input ko backend integer value me map karta hai.

6. **Result Logic**:
   - Har combination ka result check karte hain (e.g., snake vs water, gun vs snake).

7. **Error Handling**:
   - Agar koi galat condition ho, toh "Something went wrong..." print karega.

