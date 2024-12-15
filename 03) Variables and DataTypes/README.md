# Variables and DataTypes in Python

---

### **1. Variable (Memory Location ka Name)**  
Variable ek naam hota hai jo memory mein kisi value ko store karta hai.  

**Example:**  
```python
name = "Shaheer Ahmad"  # Name store ho gaya
age = 21  # Age store ho gayi
```  

---

### **2. Data Types (Data ki Categories)**  
Python khud data ka type pehchanta hai. Important types ye hain:  

1. **Integers:** Numbers bina point ke.  
2. **Floating Points:** Numbers jo point ke sath hain.  
3. **Strings:** Alphabets ya words.  
4. **Booleans:** True ya False.  
5. **None:** Khaali value.  

**Example:**  
```python
x = 10  # Integer
y = 3.14  # Float
z = "Hello"  # String
is_active = True  # Boolean
nothing = None  # NoneType
```  

---

### **3. Identifier Rules (Variable Name ke Rules)**  
1. Sirf alphabets, numbers, aur underscores use ho sakte hain.  
2. Naam alphabet ya underscore se start hona chahiye.  
3. Naam digit se start nahi ho sakta.  
4. Naam mein spaces allowed nahi hain.  

**Example:**  
```python
shaheer = 5  # Sahi
_one8 = 8  # Sahi
7name = "Galat"  # Galat (Digit se start nahi ho sakta)
```  

---

### **4. Operators (Symbols for Calculations aur Conditions)**  
Python mein ye important operators hain:  

1. **Arithmetic Operators:** `+`, `-`, `*`, `/`.  
2. **Assignment Operators:** `=`, `+=`, `-=`.  
3. **Comparison Operators:** `==`, `>`, `<`, `!=`.  
4. **Logical Operators:** `and`, `or`, `not`.  

**Logical Operators Truth Table:**  
| Operand 1 | Operand 2 | `and` | `or`  | `not Operand 1` |  
|-----------|-----------|-------|-------|-----------------|  
| True      | True      | True  | True  | False           |  
| True      | False     | False | True  | False           |  
| False     | True      | False | True  | True            |  
| False     | False     | False | False | True            |  

**Example:**  
```python
a = 10
b = 5
print(a + b)  # Arithmetic: 15
print(a > b and b > 0)  # Logical: True
```  

---

### **5. type() Function aur Typecasting (Data Type Check aur Conversion)**  
`type()` function se variable ka type check hota hai.  

**Example:**  
```python
age = 21
print(type(age))  # <class 'int'>

# Typecast Example
age_str = str(age)  # Int ko String mein convert
print(age_str)  # "21"
```  

---

### **6. input() Function (User se Input lena)**  
`input()` se user se data lete hain, jo hamesha string hota hai.  

**Example:**  
```python
name = input("Enter your name: ")  # Name input
print("Your name is " + name)  # Concatenation
```  

Agar number input lena ho:  
```python
age = int(input("Enter your age: "))  # String ko int mein convert
#suppose you enter age as 20
print(age + 5)  # Output: 25
```  

**Concatenation Example:**  
```python
first_name = "Shaheer"
last_name = "Ahmad"
full_name = first_name + " " + last_name
print(full_name)  # Output: Shaheer Ahmad
```  

---

