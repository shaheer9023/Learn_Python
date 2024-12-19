# Explanation Practice # 5

---

### **Problem 1: Urdu to English Dictionary Lookup**

**Code:**  
```python
words = {
    "pankha": "fan",
    "aalu": "potato",
    "kursi": "chair",
    "gaari": "car"
}
word = input("Wo word likho jiska matlab chahiye: ")
print(f"{word} ka matlab hai {words[word]}")
```

**Steps:**
1. **Dictionary Banai:** Humne ek dictionary `words` banayi jisme Urdu words (keys) aur unke English meanings (values) rakhe hain.
2. **User Se Input:** `input()` function se user se ek word liya jiska translation chahiye.
3. **Translation Dikhana:** Humne us input word ko dictionary `words` se lookup kiya aur translation print kar diya.

**Example:**
```
Wo word likho jiska matlab chahiye: pankha
pankha ka matlab hai fan
```

---

### **Problem 2: Unique Numbers from User Input**

**Code:**  
```python
set = set()
number = input("Enter Number: ")
set.add(int(number))
number = input("Enter Number: ")
set.add(int(number))
number = input("Enter Number: ")
set.add(int(number))
number = input("Enter Number: ")
set.add(int(number))
number = input("Enter Number: ")
set.add(int(number))
number = input("Enter Number: ")
set.add(int(number))
number = input("Enter Number: ")
set.add(int(number))
number = input("Enter Number: ")
set.add(int(number))
print(set)
```

**Steps:**
1. **Set Banaya:** Humne ek empty set `set = set()` banayi. Set ki khasiyat hai ki yeh sirf unique values store karta hai, duplicate values ko ignore karta hai.
2. **Numbers Input Karna:** Humne user se 8 baar `input()` li aur `add()` method se set mein add kiya. 
3. **Unique Values Print Karna:** Jab hum `set` ko print karte hain, to wo sirf unique values dikhayega, jo user ne enter ki.

**Example:**  
```
Enter Number: 5
Enter Number: 8
Enter Number: 5
Enter Number: 2
Enter Number: 7
Enter Number: 8
Enter Number: 9
Enter Number: 9
{2, 5, 7, 8, 9}
```

---

### **Problem 3: Set with `18` (int) and `'18'` (str)**

**Code:**  
```python
set = set()
set.add(18)
set.add("18")
print(set)
```

**Steps:**
1. **Set Banaya:** Humne ek empty set `set = set()` banayi.
2. **Add Elements:** Humne set me ek integer `18` aur ek string `"18"` add kiya.
3. **Set Ke Elements:** Python me `18` (int) aur `"18"` (string) ko alag values samajhta hai, isliye dono ko set me alag alag store kiya jaata hai.

**Example:**  
```
{18, '18'}
```

---

### **Problem 4: Set Length with Mixed Types**

**Code:**  
```python
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
```

**Steps:**
1. **Set Banaya:** Humne ek empty set `s = set()` banayi.
2. **Add Elements:** Humne 3 alag alag elements add kiye:
   - Integer `20`
   - Float `20.0` (Python me 20 aur 20.0 ko same value samjha jaata hai)
   - String `"20"`
3. **Length of Set:** Jab hum `len(s)` use karte hain to Python ye dekhta hai ki total kitne unique elements hain. `20` aur `20.0` ko same samajhne ki wajah se set me sirf 2 elements rahenge.

**Example:**  
```
2
```

---

### **Problem 5: Type of `{}`**

**Code:**  
```python
s = {}
print(type(s))
```

**Steps:**
1. **Empty Dictionary:** Humne `{}` ka use kiya jo Python me ek empty dictionary ko represent karta hai.
2. **Type Check:** `type(s)` function se humne check kiya ke `s` ka type kya hai. Is case me wo `dict` type ka object hai.

**Example:**  
```
<class 'dict'>
```

---

### **Problem 6: Favorite Languages Dictionary**

**Code:**  
```python
dict = {}
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
print(dict)
```

**Steps:**
1. **Empty Dictionary:** Humne ek empty dictionary banayi `dict = {}`.
2. **Input from User:** Humne user se friends ke naam aur unke favorite languages input liye.
3. **Dictionary Update:** Humne `update()` method ka use karke dictionary me har friend ka naam (key) aur unka favorite language (value) add kiya.
4. **Print Dictionary:** Last me humne dictionary ko print kiya.

**Example:**  
```
Enter friend's name: Ali
Enter language: Python
Enter friend's name: Ahmed
Enter language: JavaScript
Enter friend's name: Sara
Enter language: Java
Enter friend's name: Aisha
Enter language: C++
{'Ali': 'Python', 'Ahmed': 'JavaScript', 'Sara': 'Java', 'Aisha': 'C++'}
```

---

### **Problem 7: Duplicate Names in Dictionary**

**Code:**  
```python
dict = {}
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
print(dict)
```

**Steps:**
1. **Same Name:** Agar user do baar ek hi name input kare, to dictionary me usi naam ka value overwrite ho jaayega.
2. **Update Dictionary:** Agar pehle se kisi friend ka naam dictionary me ho, to wo naye language ke saath replace ho jayega.
   
**Example:**  
```
Enter friend's name: Ali
Enter language: Python
Enter friend's name: Ali
Enter language: JavaScript
{'Ali': 'JavaScript'}
```

---

### **Problem 8: Duplicate Languages in Dictionary**

**Code:**  
```python
dict = {}
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
name = input("Enter friend's name: ")
language = input("Enter language: ")
dict.update({name: language})
print(dict)
```

**Steps:**
1. **Duplicate Languages:** Agar do friends ka same language ho, to dictionary me wo alag alag entries rakh sakta hai.
   
**Example:**  
```
Enter friend's name: Ali
Enter language: Python
Enter friend's name: Ahmed
Enter language: Python
{'Ali': 'Python', 'Ahmed': 'Python'}
```

---

### **Problem 9: Lists in Set**

**Code:**  
```python
set = {8, 7, 12, "Shaheer", [1, 2]}
```

**Steps:**
1. **Set mein List Add Karne ki Koshish:** Python me set ko mutable objects (jaise list) allow nahi hote. Isliye jab hum list `[1, 2]` ko set me add karne ki koshish karte hain, to error aata hai.
   
**Example Output:**  
```
TypeError: unhashable type: 'list'
```

---

