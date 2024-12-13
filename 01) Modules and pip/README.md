

# **Modules in Python**
### Kya hain aur kaise use karein?
Modules Python mein ready-made code ka ek collection hain jo specific tasks ke liye bana hota hai.
## There are two types of modules 
- External 
- Built-in

### Common Commands:
```python
# Module ko import karna
import math  # Math functions ka module

# Specific function ko import karna
from math import sqrt  # Sirf sqrt function import

# Module ke functions ka use
print(math.pi)  # 3.141592653589793
print(sqrt(16))  # 4.0
```

### Some Built-in Modules :
- **math**: Mathematical operations ke liye.
- **random**: Random numbers generate karne ke liye.
- **datetime**: Date aur time handle karne ke liye.
- **os**: Operating system tasks ke liye.

### Common External Modules And Installation Commands:
- **numpy**: Numerical computations ke liye.
  ```bash
  pip install numpy
  ```
- **pandas**: Data analysis aur manipulation ke liye.
  ```bash
  pip install pandas
  ```
- **requests**: APIs aur web requests handle karne ke liye.
  ```bash
  pip install requests
  ```
- **flask**: Web applications banane ke liye.
  ```bash
  pip install flask
  ```
- **matplotlib**: Data visualization ke liye.
  ```bash
  pip install matplotlib
  ```

---

## 2. **Python as a Calculator**
Terminal ya Python REPL ko calculator ke tarah use kar sakte hain:

```python
# Additions
print(2 + 3)  # 5

# Multiplications
print(4 * 5)  # 20

# Exponentiation
print(2 ** 3)  # 8

# Floating-point division
print(7 / 3)  # 2.3333333333333335

# Integer division
print(7 // 3)  # 2

# Modulus (remainder)
print(7 % 3)  # 1
```

---

## 3. **REPL (Read-Evaluate-Print Loop)**
REPL ek interactive environment hai jo Python ke saath aata hai. Isme:
1. Aap code likhte hain (Read)
2. Python code ko execute karta hai (Evaluate)
3. Result show karta hai (Print)
4. Phir nayi input ka wait karta hai (Loop)

### Start karne ke liye:
```bash
python  # Ya python3 likhein terminal mein
```

Example:
```python
>>> print("Hello, World!")
Hello, World!
>>> 2 + 3
5
```

---

## 4. **Comments in Python**
Comments ka use code mein explanations likhne ke liye hota hai jo Python interpreter ignore karta hai.

### Single-line Comment
Ek line mein explanation dene ke liye `#` ka use hota hai:
```python
# Yeh ek single-line comment hai
print("Single-line comment example")
```

### Multi-line Comment
Zyada lines ke explanation ke liye triple quotes (`"""`) ka use hota hai:
```python
"""
Yeh ek multi-line comment hai
Jo zyada lines explain karne ke liye hota hai.
"""
print("Multi-line comment example")
```

---

## 5. **Syntax Error**
Agar code ka structure Python ke rules ke against ho, to syntax error aata hai.

### Example:
```python
# Syntax Error: Missing colon
if True
    print("Syntax Error Example")

# Correct Syntax:
if True:
    print("No Syntax Error")
```


