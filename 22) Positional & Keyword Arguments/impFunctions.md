

1. **`enumerate()`** → List ke elements ke sath **index number** return karta hai.  
2. **`min()`** → Do numbers ka **chhota value return** karta hai.  
3. **`list()`** → Kisi bhi **iterable (tuple, dictionary keys/values)** ko **list me convert** karta hai.  
4. **`.keys()` & `.values()`** → Dictionary ke **keys aur values ko access** karne ke liye use hota hai.  
5. **`f-string`** → Strings ko format karne ke liye use hota hai taake variables ko directly include kiya ja sake.

---

## **🔹 1. `enumerate()` → Index & Value Sath Return Karta Hai**
✅ **Yeh function ek iterable (list, tuple, etc.) ke har element ke sath ek index number bhi return karta hai.**

### **Example:**
```python
names = ["Anas", "Shaheer", "Ahmad"]

for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")
```
### **Output:**
```
Index: 0, Name: Anas
Index: 1, Name: Shaheer
Index: 2, Name: Ahmad
```
📌 **Kaise Kaam Karta Hai?**
| Iteration | `index` | `name` |
|-----------|--------|---------|
| 1st       | 0      | "Anas"  |
| 2nd       | 1      | "Shaheer" |
| 3rd       | 2      | "Ahmad" |

---

## **🔹 2. `min()` → Do Numbers Me Se Chhoti Value Deta Hai**
✅ **Yeh function do ya zyada numbers ka comparison karta hai aur sabse chhoti value return karta hai.**

### **Example:**
```python
a = 10
b = 5

print(min(a, b))  # Chhoti value print hogi
```
### **Output:**
```
5
```

📌 **Iska Use Code Me Kyu Kiya?**
```python
min_length = min(len(names), len(departments))
```
- **Agar names aur departments ki length match nahi karti**, to sirf chhoti length tak loop chale.  
- Yeh **errors ko prevent** karta hai.

---

## **🔹 3. `list()` → Iterable Ko List Me Convert Karta Hai**
✅ **Yeh kisi bhi iterable ko list me convert karta hai, jaise tuple ya dictionary keys/values.**

### **Example:**
```python
tuple_data = (1, 2, 3)
converted_list = list(tuple_data)

print(converted_list)
```
### **Output:**
```
[1, 2, 3]
```

📌 **Iska Use Code Me Kyu Kiya?**
```python
dept_name = list(departments.keys())[i]
dept_field = list(departments.values())[i]
```
- **`departments.keys()` dictionary ke sab keys ka ek view object return karta hai**, jo **list nahi hota**.  
- **List me convert karna zaroori hai taake uska index access kar sakein**.

---

## **🔹 4. `.keys()` & `.values()` → Dictionary Ki Keys Aur Values Extract Karna**
✅ **Yeh function dictionary ke andar se keys aur values ko extract karne ke liye use hota hai.**

### **Example:**
```python
departments = {"Master": "AI", "ADP": "CS", "Research": "ML"}

print(departments.keys())   # Sirf keys print karega
print(departments.values()) # Sirf values print karega
```
### **Output:**
```
dict_keys(['Master', 'ADP', 'Research'])
dict_values(['AI', 'CS', 'ML'])
```

📌 **Iska Use Code Me Kyu Kiya?**
```python
dept_name = list(departments.keys())[i]
dept_field = list(departments.values())[i]
```
- **Keys aur values ko access karne ke liye list me convert karna zaroori hai**, warna hum direct indexing nahi kar sakte.

---

## **🔹 5. `f-string` → Variables Ko String Me Inject Karna**
✅ **`f-string` ek fast aur easy tareeqa hai variables ko string ke andar use karne ka.**

### **Example:**
```python
name = "Shaheer"
age = 20

print(f"My name is {name} and I am {age} years old.")
```
### **Output:**
```
My name is Shaheer and I am 20 years old.
```

📌 **Iska Use Code Me Kyu Kiya?**
```python
print(f"Name: {name} | Language: {language} | Department: {dept_name} - {dept_field}")
```
- **Readable aur clean output generate karne ke liye**.

---

## **🔹 Final Summary**
| Function | Purpose | Example |
|----------|---------|---------|
| **`enumerate()`** | List ke sath index return karta hai | `enumerate(names)` |
| **`min()`** | Sabse chhoti value return karta hai | `min(5, 10)` → `5` |
| **`list()`** | Kisi bhi iterable ko list me convert karta hai | `list(departments.keys())` |
| **`.keys()` & `.values()`** | Dictionary se keys aur values extract karta hai | `departments.keys()` |
| **`f-string`** | Variables ko string me inject karta hai | `f"Hello {name}"` |