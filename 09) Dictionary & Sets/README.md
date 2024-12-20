# Dictionary in Python
Dictionary ka matlab hai ek collection jo keys aur unki corresponding values ko store karta hai.

Syntax:
```python
a = { 
    "key": "value",
    "shaheer": "code",
    "marks": "100",
    "list": [1, 2, 9] 
}
print(a["key"])  # Output: "value"
print(a["list"]) # Output: [1, 2, 9]
```

PROPERTIES OF PYTHON DICTIONARIES

1. Yeh unordered hote hain (matlab kisi specific order mein nahi hote).
2. Yeh mutable hote hain (values ko update kiya ja sakta hai).
3. Yeh indexed hote hain (keys ke zariye access karte hain).
4. Duplicate keys allowed nahi hoti.

DICTIONARY METHODS

Consider the following dictionary:
```python
a = {
    "name": "shaheer",
    "from": "pakistan",
    "marks": [92, 98, 96]
}
```

### 1. items() Method
Code Example:
```python
# items() method key-value pairs ko list of tuples mein return karta hai.
print(a.items())
```
Output:
```
dict_items([(\"name\", \"shaheer\"), (\"from\", \"pakistan\"), (\"marks\", [92, 98, 96])])
```
Explanation:
`items()` dictionary ke andar ke tamam key-value pairs ko list of tuples ke form mein dikhata hai.

### 2. keys() Method
Code Example:
```python
# keys() method dictionary ki sirf keys ki list return karta hai.
print(a.keys())
```
Output:
```
dict_keys(['name', 'from', 'marks'])
```
Explanation:
`keys()` method se aapko dictionary mein mojood tamam keys ki list milti hai.

### 3. values() Method
Code Example:
```python
# values() method dictionary ki values ko list ke form mein return karta hai.
print(a.values())
```
Output:
```
dict_values(['shaheer', 'pakistan', [92, 98, 96]])
```
Explanation:
`values()` method dictionary mein jitni values hain unka ek list return karta hai.

### 4. update() Method
Code Example:
```python
# update() method naye key-value pair ko dictionary mein add karta hai ya existing ko update karta hai.
a.update({"friends": "Ali"})
print(a)
```
Output:
```
{'name': 'shaheer', 'from': 'pakistan', 'marks': [92, 98, 96], 'friends': 'Ali'}
```
Explanation:
`update()` se dictionary mein naye elements add ya existing elements update hote hain.

### 5. get() Method
Code Example:
```python
# get() method specified key ka value return karta hai.
print(a.get("name"))
```
Output:
```
shaheer
```
Explanation:
`get()` method specified key ka value return karta hai. Agar key exist nahi karti toh `None` return hota hai.

### 6. pop() Method
Code Example:
```python
# pop() method specified key ka value return karta hai aur us key-value pair ko dictionary se remove karta hai.
removed_value = a.pop("marks")
print(removed_value)  # Output: [92, 98, 96]
print(a)              # Output: {'name': 'shaheer', 'from': 'pakistan'}
```
Explanation:
`pop()` method ek specified key ko remove karta hai aur uska value return karta hai.

### 7. popitem() Method
Code Example:
```python
# popitem() method last inserted key-value pair ko remove aur return karta hai.
last_item = a.popitem()
print(last_item)
print(a)
```
Output:
```
("friends", "Ali")
{'name': 'shaheer', 'from': 'pakistan'}
```
Explanation:
`popitem()` method dictionary ka last inserted key-value pair remove karta hai aur usay tuple ke form mein return karta hai.

### 8. clear() Method
Code Example:
```python
# clear() method poori dictionary ko khali kar deta hai.
a.clear()
print(a)
```
Output:
```
{}
```
Explanation:
`clear()` method dictionary ke tamam elements ko remove karta hai aur usay empty kar deta hai.

---

# SETS IN PYTHON

Set ek aisi collection hai jo sirf unique (non-repetitive) elements ko store karta hai.

Example:
```python
set1 = set()  # Empty set
set1.add(1)
set1.add(2)
print(set1)  # Output: {1, 2}
```

PROPERTIES OF SETS

1. Sets unordered hote hain (element order matter nahi karta).
2. Sets unindexed hote hain (index se access nahi kar sakte).
3. Sets ke elements change nahi kiye ja sakte.
4. Sets duplicate values store nahi karte.

### OPERATIONS ON SETS
Consider the following set:
```python
s = {1, 8, 2, 3}
```

### 1. len() Method
Code Example:
```python
# len() method set ke elements ki total count return karta hai.
print(len(s))
```
Output:
```
4
```
Explanation:
`len()` set ke andar jitne elements hain unki count return karta hai.

### 2. add() Method
Code Example:
```python
# add() method set mein ek naya element add karta hai.
s.add(5)
print(s)
```
Output:
```
{1, 2, 3, 5, 8}
```
Explanation:
`add()` method se set mein ek naya element insert kiya jata hai.

### 3. remove() Method
Code Example:
```python
# remove() method specified element ko set se hata deta hai.
s.remove(8)
print(s)
```
Output:
```
{1, 2, 3}
```
Explanation:
`remove()` specified element ko set se delete karta hai. Agar element nahi mila toh error throw karega.

### 4. discard() Method
Code Example:
```python
# discard() method specified element ko remove karta hai. Agar element nahi mila toh error nahi throw karta.
s.discard(2)
s.discard(10)  # No error
print(s)
```
Output:
```
{1, 3}
```
Explanation:
`discard()` method remove ki tarah kaam karta hai, lekin agar element nahi mila toh error throw nahi karta.

### 5. pop() Method
Code Example:
```python
# pop() method randomly ek element remove karta hai aur uska value return karta hai.
removed_element = s.pop()
print(removed_element)
print(s)
```
Output:
```
1 (ya koi aur random element)
Updated set
```
Explanation:
`pop()` set se ek random element delete karta hai aur uska value return karta hai.

### 6. clear() Method
Code Example:
```python
# clear() method set ke tamam elements ko remove karke usay empty kar deta hai.
s.clear()
print(s)
```
Output:
```
set()
```
Explanation:
`clear()` method set ke tamam elements ko khatam kar deta hai aur empty set return karta hai.

### 7. union() Method
Code Example:
```python
# union() method do sets ke unique elements ko merge karta hai.
print(s.union({8, 11}))
```
Output:
```
{1, 2, 3, 8, 11}
```
Explanation:
`union()` do sets ke tamam unique elements ko combine karta hai.

### 8. intersection() Method
Code Example:
```python
# intersection() method sirf dono sets ke common elements return karta hai.
print(s.intersection({2, 3}))
```
Output:
```
{2, 3}
```
Explanation:
`intersection()` method sirf un elements ko return karta hai jo dono sets mein common hote hain.

---
Zyada methods ke liye Python documentation visit karein.

