# Practice # 8 Explanation

---

## Problem 1: Find Greatest of Three Numbers

### Explanation:
Yeh function user se 3 numbers input leta hai aur unka comparison karke sabse bara number print karta hai.

### Code:
```python
def greatest():
    # User se 3 numbers ka input lena
    one = int(input("Enter 1st number: "))  # Pehla number input karein
    second = int(input("Enter 2nd number: "))  # Dusra number input karein
    third = int(input("Enter 3rd number: "))  # Teesra number input karein
    # Numbers ka comparison karte hain
    if one > second and one > third:  # Agar pehla number dusre aur teesre number se bara ho
        print(f"{one} is greatest.")  # Pehla number greatest hai
    elif second > one and second > third:  # Agar dusra number pehle aur teesre number se bara ho
        print(f"{second} is greatest.")  # Dusra number greatest hai
    else:  # Agar teesra number sabse bara ho
        print(f"{third} is greatest.")  # Teesra number greatest hai

greatest()
```

### Input:
```
Enter 1st number: 45
Enter 2nd number: 12
Enter 3rd number: 30
```

### Output:
```
45 is greatest.
```

---

## Problem 2: Convert Celsius to Fahrenheit

### Explanation:
Yeh function Celsius temperature ko Fahrenheit me convert karta hai.

### Code:
```python
def convert():
    # User se Celsius temperature ka input lena
    temperature = float(input("Enter Temperature in Celsius: "))  # Celsius temperature input karein
    # Celsius se Fahrenheit ka conversion formula
    fahrenheit = (temperature * 9 / 5) + 32  # Conversion formula ka use karein
    print(f"Fahrenheit temperature is: {fahrenheit}")  # Fahrenheit temperature print karein

convert()
```

### Input:
```
Enter Temperature in Celsius: 25
```

### Output:
```
Fahrenheit temperature is: 77.0
```

---

## Problem 3: Prevent New Line in print()

### Explanation:
Python ka `print()` function default me new line dalta hai. `end` parameter ka use karke is behavior ko prevent karte hain.

### Code:
```python
print("Shaheer")  # Pehle line me "Shaheer" print karein
print("Ahmad")  # Doosre line me "Ahmad" print karein
# Ab new line prevent karte hain
print("Shaheer", end="")  # "Shaheer" ke baad new line na dalein
print(" Ahmad")  # " Ahmad" ko usi line me add karein
```

### Output:
```
Shaheer
Ahmad
Shaheer Ahmad
```

---

## Problem 4: Recursive Function to Calculate Sum of First n Natural Numbers

### Explanation:
Yeh function recursion ka use karke pehle n natural numbers ka sum calculate karta hai.

### Code:
```python
def sum_natural(number):
    # Base case jab number 1 ho
    if number == 1:  # Agar number 1 hai
        return 1  # To 1 return karein
    else:
        # Recursion ka use karke sum calculate karein
        return number + sum_natural(number - 1)  # Current number aur remaining numbers ka sum return karein

number = int(input("Enter a number: "))  # User se n ka input lena
print(f"Sum of first {number} natural numbers is {sum_natural(number)}")  # Result print karein
```

### Input:
```
Enter a number: 5
```

### Output:
```
Sum of first 5 natural numbers is 15
```

---

## Problem 5: Print Pattern of Stars

### Explanation:
Yeh function reverse triangular pattern of stars print karta hai.

### Code:
```python
def stars():
    # User se number of lines ka input lena
    n = int(input("Enter number of stars: "))  # Number of lines input karein
    for i in range(n, 0, -1):  # Loop reverse direction me chalega
        print("*" * i)  # Har line me i stars print karein

stars()
```

### Input:
```
Enter number of stars: 3
```

### Output:
```
***
**
*
```

---

## Problem 6: Convert Inches to Centimeters

### Explanation:
Yeh function inches ko centimeters me convert karta hai.

### Code:
```python
def convert_to_cm():
    # User se inches ka input lena
    inches = float(input("Enter length in inches: "))  # Length in inches input karein
    # Inches ko centimeters me convert karna
    cms = inches * 2.54  # Conversion formula ka use karein
    print(f"Length in centimeters is: {cms}")  # Result print karein

convert_to_cm()
```

### Input:
```
Enter length in inches: 12
```

### Output:
```
Length in centimeters is: 30.48
```

---

## Problem 7: Remove a Given Word from a List and Strip Extra Spaces
Here is your original code with the required explanation in Roman Urdu for each line:

---

## Problem 7: Remove a Given Word from a List and Strip Extra Characters


```python
# Ek function define karte hain jo list se ek specific word ko remove karega aur saath hi strip bhi karega
def stripping(list, wordToRemove):
    newList = []  # Ek nayi khali list banate hain
    for item in list:  # Har item ke liye list par loop chalate hain
        if item != wordToRemove:  # Agar current item wordToRemove ke barabar nahi hai
            newList.append(item.strip(wordToRemove))  # Item ko strip karke nayi list me add karte hain
    return newList  # Final list return karte hain

# Ek list define karte hain
list = ["shaheer", "ahmad", "anas", "zaid"]  # Original list
# Function ko call karke result print karte hain
print(stripping(list, "d"))
```

---

### Input:
```
Original list: ["shaheer", "ahmad", "anas", "zaid"]
Word to remove: "d"
```

---

### Output:
```
['shaheer', 'ahma', 'anas', 'zai']
```

---


## Problem 8: Print Multiplication Table of a Given Number

### Explanation:
Yeh function kisi bhi number ka multiplication table print karta hai.

### Code:
```python
def multiplication_table():
    number = int(input("Enter a number: "))  # User se number input lena
    for i in range(1, 11):  # 1 se 10 tak loop lagana
        print(f"{number} x {i} = {i * number}")  # Table ka result print karna

multiplication_table()
```

### Input:
```
Enter a number: 7
```

### Output:
```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

