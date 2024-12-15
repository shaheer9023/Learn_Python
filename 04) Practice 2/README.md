# Explanation of Practice # 2

---

### Problem 1: Adding Two Numbers

```python
# User se pehla number lena
one = int(input("enter 1st number : "))  # User input ko integer me convert karna
# User se doosra number lena
second = int(input("enter 2nd number : "))  # User input ko integer me convert karna
# Dono numbers ka jam'a nikaal kar print karna
print("The sum of ", one, " and ", second, " is : ", one + second)
```

### Explanation:
1. **User Input**: Pehle, pehla number user se `input()` function se lete hain aur isay integer (`int`) me convert karte hain.
   - **Example Input**: If the user inputs `10`.
2. **Second Number**: Phir doosra number lete hain.
   - **Example Input**: If the user inputs `20`.
3. **Calculation and Output**: Dono numbers ka sum nikaal kar output screen par print karte hain.
   - **Expected Output**: `The sum of  10  and  20  is :  30`

---

### Problem 2: Finding the Remainder

```python
# User se koi number lena
number = int(input("enter any number : "))  # Input ko integer me convert karna
# Random variable z ki value set karna
z = 5  
# Modulus operator % istemal karke remainder nikaalna
print("the remainder on number = ", number, " when divided by z = ", z, " is = ", number % z)
```

### Explanation:
1. **User Input**: User se koi number lete hain aur isay integer me convert karte hain.
   - **Example Input**: If the user inputs `23`.
2. **Fixed Value for Division**: `z` ki value ko 5 set karte hain.
3. **Remainder Calculation**: Modulus operator (`%`) istemal kar ke remainder nikaalne aur print karte hain.
   - **Expected Output**: For the input `23`, the output would be `the remainder on number =  23  when divided by z =  5  is =  3`

---

### Problem 3: Checking Variable Type

```python
# User se koi variable lena
variable = input("enter any variable : ")  # Default input string hota hai
# Variable ka type check karna
print("type of variable is : ", type(variable))  # Type always <class 'str'> hota hai
# Type conversion karna
variable2 = int(variable)  # Isay integer me convert karte hain
# Naya type check karna
print("after type conversion the above type is changed to : ", type(variable2))  # Ab type <class 'int'> hoga
```

### Explanation:
1. **User Input**: User se koi variable lete hain.
   - **Example Input**: If the user inputs `45`.
2. **Type Checking**: Pehle variable ka type check karte hain, jo `str` hoga.
   - **Expected Output**: `type of variable is : <class 'str'>`
3. **Type Conversion**: Variable ko integer me convert karne ke baad phir is ka type nikaalte hain.
   - **Expected Output**: `after type conversion the above type is changed to : <class 'int'>`

---

### Problem 4: Comparing Two Variables

```python
# a aur b ki values set karna
a = 34
b = 80
# Comparison operator se check karna
result = a > b  # yeh check karta hai ke a b se bada hai ya nahi
# Result ko print karna
print(result)  # Output false hoga
```

### Explanation:
1. **Variable Declaration**: `a` aur `b` ko set karte hain (34 aur 80).
2. **Comparison**: `a` ko `b` se compare karte hain aur result store karte hain.
   - **Expected Output**: Since `34` is not greater than `80`, the result will be `False`.
3. **Output Result**: Result ko print karte hain.
   - **Final Output**: `False`

---

### Problem 5: Calculating the Average

```python
# User se do numbers lena
one = int(input("enter 1st number : "))  # Pehla number input karna
second = int(input("enter 2nd number : "))  # Doosra number input karna
# Average nikaalna
print("The average of ", one, " and ", second, " is : ", (one + second) / 2)  # Do numbers ka average
```

### Explanation:
1. **User Input**: Do numbers user se lete hain.
   - **Example Input**: If the user inputs `10` and `30`.
2. **Average Calculation**: Average nikaalne ke liye dono numbers ka sum ko 2 se divide karte hain.
   - **Expected Output**: For the inputs `10` and `30`, the output would be `The average of  10  and  30  is :  20.0`

---

### Problem 6: Calculating Powers of a Number

```python
# User se ek number lena
number = int(input("enter any number : "))  # Input ko integer me convert karna
# Number ke powers nikaalna
print("the square of given number is ", number ** 2)  # Square nikaalna
print("\nthe cube of given number is ", number ** 3)  # Cube nikaalna
print("\nthe power 4 of given number is ", number ** 4)  # Power 4 nikaalna
print("\n and so on .......")  # Aur bhi aage ki powers nikaal sakte hain
```

### Explanation:

#### Note : Power dene k liye `**` use hota h 
1. **User Input**: User se ek number lete hain.
   - **Example Input**: If the user inputs `3`.
2. **Power Calculations**: 
   - Square: \(3^2 = 9\)
   - Cube: \(3^3 = 27\)
   - Fourth Power: \(3^4 = 81\)

   - **Expected Output**: 
     - `the square of given number is  9`
     - `the cube of given number is  27`
     - `the power 4 of given number is  81`
     - `and so on .......`

---

