# Explanation Practice # 3

---

## Problem 1: User Input aur String Display  

### Code:
```python
name = input("enter your name ")
print("Good Afternoon "+name)
# Using f-string
print(f"Good Afternoon {name}")
```

### Explanation:
1. **`input()` function**: Yeh user se input lene ke liye hota hai.
   - Example Input: `Shaheer Ahmad`
2. **String Concatenation**: `"Good Afternoon " + name` iska matlab dono strings ko jod dena.
3. **f-string**: Isko format string kehte hain. `{}` ke andar variable likhne se wo directly value insert kar deta hai.  
   - Output:  
   ```
   Good Afternoon Shaheer Ahmad
   Good Afternoon Shaheer Ahmad
   ```

---

## Problem 2: Replace Function se Template Fill Karna  

### Code:
```python
letter = ''' Dear <|Name|>,
 You are selected!
   <|Date|> '''

print(letter.replace("<|Name|>", "Shaheer Ahmad").replace("<|Date|>", "December 16,2024"))
```

### Explanation:
1. **Template**: Letter ke andar placeholders hain (`<|Name|>` aur `<|Date|>`).
2. **`replace()` function**: Yeh string ke andar ek text ko doosre text se replace karta hai.
   - Example: `<|Name|>` ko `"Shaheer Ahmad"` se replace karega.
   - `<|Date|>` ko `"December 16,2024"` se replace karega.
3. **Output**:  
   ```
   Dear Shaheer Ahmad,
    You are selected!
      December 16,2024
   ```

---

## Problem 3: Double Space Detect Karna  

### Code:
```python
string = "Shaheer is not a good  boy"
print(string.find("  "))

emogi = "❤ ❤ ❤  ❤"
print(emogi.find("  ")) #5
```

### Explanation:
1. **`find()` function**: Yeh pehle position batata hai jahaan search wala string milta hai.
   - **Double Space** ka index return hota hai.
2. **Example 1**:  
   - Input: `"Shaheer is not a good  boy"`  
   - Output: `21`  
3. **Example 2**:  
   - Input: `"❤ ❤ ❤  ❤"`  
   - Output: `5`  

---

## Problem 4: Double Space Ko Replace Karna  

### Code:
```python
string = "Shaheer is not a good  boy"
print(string.replace("  ", " "))

emogi = "❤ ❤ ❤  ❤"
print(emogi.replace("  ", " "))
print(emogi)  # original string change nahi hogi
```

### Explanation:
1. **`replace()` function**: Double space ko single space se replace karta hai.
2. **Original String**: `replace()` original string ko change nahi karta.  
   - Example: `"❤ ❤ ❤  ❤"` string ke andar double space ko single space kar diya.
3. **Output**:  
   ```
   Shaheer is not a good boy
   ❤ ❤ ❤ ❤
   ❤ ❤ ❤  ❤
   ```

---

## Problem 5: Escape Sequences Se Formatting  

### Code:
```python
letter = "Dear Shaheer, this python course is nice. Thanks!"
print(letter)

formatedletter = "Dear Shaheer,\n\t this python course is nice.\n Thanks!"
print(formatedletter)
```

### Explanation:
1. **Escape Sequences**: Special characters jo string ko format karte hain:
   - `\n`: Naya line.
   - `\t`: Tab space deta hai.
2. **Output**:  
   **Without Formatting**:  
   ```
   Dear Shaheer, this python course is nice. Thanks!
   ```
   **With Formatting**:  
   ```
   Dear Shaheer,
        this python course is nice.
    Thanks!
   ```

---

### **Summarized Input/Output Table**

| **Problem** | **Example Input**           | **Output**                                 |
|-------------|-----------------------------|-------------------------------------------|
| **1**       | `Shaheer Ahmad`             | Good Afternoon Shaheer Ahmad              |
| **2**       | N/A                         | Dear Shaheer Ahmad, <br> You are selected! <br> December 16,2024 |
| **3**       | `"Shaheer is not a good  boy"` | `21`                                     |
| **4**       | `"❤ ❤ ❤  ❤"`               | `❤ ❤ ❤ ❤`                                |
| **5**       | N/A                         | Dear Shaheer, <br> this python course is nice. <br> Thanks! |

---

**Yeh tha har problem ka short Roman Urdu explanation aur output! Agar aur kisi cheez ki zarurat ho to batayein. 😊**