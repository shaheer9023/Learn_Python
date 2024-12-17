# Explanation Practice # 4
### **Problem 1: Store seven fruits in a list entered by the user**

#### **Code**:
```python
fruits = []
f1 = input("Enter fruit name 1: ")
fruits.append(f1)
f2 = input("Enter fruit name 2: ")
fruits.append(f2)
f3 = input("Enter fruit name 3: ")
fruits.append(f3)
f4 = input("Enter fruit name 4: ")
fruits.append(f4)
f5 = input("Enter fruit name 5: ")
fruits.append(f5)
f6 = input("Enter fruit name 6: ")
fruits.append(f6)
f7 = input("Enter fruit name 7: ")
fruits.append(f7)
print(fruits)
```

#### **Explanation**:
1. Empty list `fruits` banayi gayi.
2. `input()` function se 7 fruits ka naam user se liya aur `append()` se list me add kiya.
3. Last me `print()` se poori list ko display kiya.

#### **Output**:
```
Enter fruit name 1: Apple  
Enter fruit name 2: Banana  
Enter fruit name 3: Mango  
Enter fruit name 4: Grapes  
Enter fruit name 5: Orange  
Enter fruit name 6: Kiwi  
Enter fruit name 7: Pineapple  

['Apple', 'Banana', 'Mango', 'Grapes', 'Orange', 'Kiwi', 'Pineapple']
```

---

### **Problem 2: Accept marks of 6 students and display them sorted**

#### **Code**:
```python
marks = []
f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter marks here: "))
marks.append(f5)
f6 = int(input("Enter marks here: "))
marks.append(f6)
marks.sort()
print(marks)
```

#### **Explanation**:
1. Empty list `marks` banayi gayi.
2. `input()` function se 6 students ke marks liye gaye aur `append()` ka use kiya list me store karne ke liye.
3. `sort()` method ka use karke marks ko ascending order me arrange kiya.
4. Last me `print()` se sorted list display ki.

#### **Output**:
```
Enter marks here: 78  
Enter marks here: 90  
Enter marks here: 56  
Enter marks here: 89  
Enter marks here: 45  
Enter marks here: 67  

[45, 56, 67, 78, 89, 90]
```

---

### **Problem 3: Check that a tuple type cannot be changed**

#### **Code**:
```python
tuple = ("shaheer", 21)
tuple[0] = "Anas"  # TypeError: 'tuple' object does not support item assignment
print(tuple)
```

#### **Explanation**:
1. Tuple `("shaheer", 21)` banayi gayi.
2. Jab tuple ke pehle element ko `tuple[0] = "Anas"` ke through change karne ki koshish ki gayi, toh `TypeError` aayi kyunki tuples immutable (unchangeable) hote hain.

#### **Output**:
```
TypeError: 'tuple' object does not support item assignment
```

---

### **Problem 4: Sum a list with 4 numbers**

#### **Code**:
```python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Sum of list is {sum(list)}")
```

#### **Explanation**:
1. Ek list `list` me numbers store kiye gaye.
2. `sum()` function ka use karke list ke elements ka sum calculate kiya.
3. Result ko `print()` se display kiya.

#### **Output**:
```
Sum of list is 55
```

---

### **Problem 5: Count the number of zeros in a tuple**

#### **Code**:
```python
tuple = (7, 0, 8, 0, 0, 9)
print(f"Total number of zeros in tuple is {tuple.count(0)}")
```

#### **Explanation**:
1. Ek tuple `(7, 0, 8, 0, 0, 9)` banayi gayi.
2. `count(0)` method ka use karke tuple me zeros ko count kiya gaya.
3. Result ko `print()` ke zariye display kiya.

#### **Output**:
```
Total number of zeros in tuple is 3
```