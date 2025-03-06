### **🔹 `*args` aur `**kwargs` Kya Hain?**
Agar aap Python me **function** likh rahe hain, lekin aap **pehle se nahi jaante ke kitne arguments aayenge**, tab aap **`*args` aur `**kwargs` ka use karte hain**.

✅ **`*args` → Multiple values (tuple me store hoti hain)**  
✅ **`**kwargs` → Multiple key-value pairs (dictionary me store hote hain)**  



---

## **🔸 `*args` Kya Hai? (Jab Multiple Values Aayengi)**
Jab aap function ko call karein, aur **multiple values pass karein** bina `list` ya `tuple` banaye, to aap `*args` use kar sakte hain. **Yeh sari values ek tuple me store hoti hain.**

📌 **Samajhne ka Asaan Tarika:**  
Agar aapko ek function likhna hai jo **jitne marzi numbers ka sum** kare, lekin aap nahi jaante ke kitne numbers honge, tab `*args` use karein.

### **✅ Example:**
```python
def total_sum(*numbers):
    print(f"Ye numbers aaye hain: {numbers}")  # Tuple ki tarah store hotay hain
    return sum(numbers)  # Sab numbers ka sum karega

result = total_sum(10, 20, 30, 40, 50)
print(f"Total Sum: {result}")
```

### **✅ Output:**
```
Ye numbers aaye hain: (10, 20, 30, 40, 50)
Total Sum: 150
```

✅ **Matlab:** Aap jitne chahein numbers pass kar sakte hain, aur wo **tuple** (`(10, 20, 30, 40, 50)`) me store ho jate hain.  

---

## **🔸 `**kwargs` Kya Hai? (Jab Multiple Key-Value Pairs Aayengi)**
Jab aap function ko call karein, aur **key-value pairs** pass karein, to `**kwargs` use hota hai. **Yeh sari values ek dictionary me store hoti hain.**

📌 **Samajhne ka Asaan Tarika:**  
Agar aap ek function likhna chahte hain jo **student ka naam, age aur city store kare**, aur aap nahi jaante ke aur kitni extra details hongi, to `**kwargs` use karein.

### **✅ Example:**
```python
def student_info(**details):
    print(f"Student Details: {details}")  # Dictionary ki tarah store hotay hain
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Ali", age=20, city="Lahore")
```

### **✅ Output:**
```
Student Details: {'name': 'Ali', 'age': 20, 'city': 'Lahore'}
name: Ali
age: 20
city: Lahore
```

✅ **Matlab:** Aap jitne chahein **key-value pairs** pass kar sakte hain, aur wo **dictionary** (`{'name': 'Ali', 'age': 20, 'city': 'Lahore'}`) me store ho jate hain.

---

## **🎯 `*args` aur `**kwargs` Dono Ek Sath**
Agar aap function me **positional arguments** bhi aur **keyword arguments** bhi bhejna chahte hain, to dono ka combination use kar sakte hain.

📌 **Samajhne ka Asaan Tarika:**  
Agar aap ek function likhna chahte hain jo **course ka naam, students ke naam aur teacher ka naam** store kare, tab aap `*args` aur `**kwargs` dono ek saath use kar sakte hain.

### **✅ Example:**
```python
def display_info(course, *students, **details):
    print(f"Course: {course}")
    print(f"Students: {students}")  # Tuple me store honge
    print(f"Details: {details}")  # Dictionary me store honge

display_info("Python", "Ali", "Ahmed", "Sara", instructor="Hassan", duration="3 Months")
```

### **✅ Output:**
```
Course: Python
Students: ('Ali', 'Ahmed', 'Sara')
Details: {'instructor': 'Hassan', 'duration': '3 Months'}
```

✅ **Matlab:**  
1. `"Python"` → **Simple argument hai** jo course ka naam store karega.  
2. `"Ali", "Ahmed", "Sara"` → **Ye `*args` me store ho jayenge tuple ki tarah.**  
3. `instructor="Hassan", duration="3 Months"` → **Ye `**kwargs` me store ho jayenge dictionary ki tarah.**  

---

## **🎯 `*args` aur `**kwargs` Kyu Use Karte Hain?**
✔ Jab hume **pehle se nahi pata hota kitne arguments** function me pass honge.  
✔ Jab hume **flexibility** chahiye ke function har type ke data ko accept kare.  
✔ Jab hume **dynamic aur reusable functions** likhne hote hain.  

