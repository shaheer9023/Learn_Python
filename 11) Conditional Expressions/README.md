# Conditional Expressions in Python
- Kabhi kabhi hum PUBG khelte hain agar din Sunday ho.

- Kabhi kabhi hum Ice Cream online order karte hain agar din sunny ho.

- Kabhi kabhi hum hiking pe jate hain agar hamare parents allow karen.

- Ye sab decisions hain jo kisi condition ke puray hone par depend karte hain. Python programming mein bhi hum instructions ko condition(s) ke puray hone par execute karte hain. Isi kaam ke liye conditionals use hote hain!

**IF ELSE AUR ELIF PYTHON MEIN**

If, else aur elif statements ka use program mein multiway decision lene ke liye hota hai jab specific conditions puri hoti hain.

### Syntax:
```python
if (condition1):  # agar condition1 True ho
    print("yes")
elif (condition2):  # agar condition2 True ho
    print("no")
else:  # agar dono conditions fail ho jayein
    print("maybe")
```

### Code Example:
```python
a = 22

if a > 9:
    print("greater")
else:
    print("lesser")
```

**Output:**
```
greater
```

### Quick Quiz:
Ek program likhein jo "yes" print kare jab user ki entered age 18 ya us se zyada ho.

#### Solution:
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("yes")
else:
    print("no")
```

**Output Example:**
```
Enter your age: 20
yes
```

### Relational Operators:
Relational Operators if statements ke andar conditions evaluate karte hain. Kuch examples:

- `==`: Equals
- `>=`: Greater than or equal to
- `<=`: Lesser than or equal to

### Logical Operators:
Python mein logical operators conditional statements par operate karte hain. Examples:

- `and`: True agar dono operands true hain, warna false.
- `or`: True agar kam se kam ek operand true ho, warna false.
- `not`: True ko false aur false ko true mein convert karta hai.

### ELIF Clause:
`elif` ka matlab hai "else if." Agar multiple conditions chain karni ho, to if statements ke saath elif aur else ka use hota hai.

#### Syntax:
```python
if (condition1):
    # code
elif (condition2):
    # yeh ladder tabhi rukega jab if ya elif ki koi condition true ho
    # code
elif (condition3):
    # code
else:
    # code
```

### Important Notes:
1. `elif` statements ki koi limit nahi hai; jitne marzi likhe ja sakte hain.
2. Last `else` tabhi execute hoga jab sab elif conditions fail ho jayein.

