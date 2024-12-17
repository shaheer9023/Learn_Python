# Python Lists & Tuples Explanation
******Python lists****** are containers to store a set of values of any data type.


**LIST INDEXING**

A list can be indexed just like a string.

```python
l1 = [7, 9, "shaheer"]

l1[0] # 7
l1[1] # 9
l1[70] # error
l1[0:2] # [7, 9] # list slicing
```

### LIST METHODS.
Consider the following list:

```python
l1 = [1, 8, 7, 2, 21, 15]
```

1. **`l1.sort()`**
   Updates the list to sorted order.

   ```python
   l1.sort()
   print(l1)  # [1, 2, 7, 8, 15, 21]
   ```

   **Roman Urdu:** `sort()` list ko ascending order mein arrange karta hai.

2. **`l1.reverse()`**
   Reverses the list.

   ```python
   l1.reverse()
   print(l1)  # [15, 21, 2, 7, 8, 1]
   ```

   **Roman Urdu:** `reverse()` list ke order ko ulta karta hai.

3. **`l1.append(8)`**
   Adds 8 at the end of the list.

   ```python
   l1.append(8)
   print(l1)  # [15, 21, 2, 7, 8, 1, 8]
   ```

   **Roman Urdu:** `append()` list ke end par element add karta hai.

4. **`l1.insert(3, 8)`**
   Adds 8 at index 3.

   ```python
   l1.insert(3, 8)
   print(l1)  # [15, 21, 2, 8, 7, 8, 1]
   ```

   **Roman Urdu:** `insert()` kisi bhi index par element insert karne ke liye use hota hai.

5. **`l1.pop(2)`**
   Deletes the element at index 2 and returns its value.

   ```python
   value = l1.pop(2)
   print(value)  # 2
   print(l1)  # [15, 21, 8, 7, 8, 1]
   ```

   **Roman Urdu:** `pop()` kisi index ka element remove kar deta hai.

6. **`l1.remove(21)`**
   Removes the first occurrence of 21.

   ```python
   l1.remove(21)
   print(l1)  # [15, 8, 7, 8, 1]
   ```

   **Roman Urdu:** `remove()` specific element ko list se hata deta hai.

7. **`len(list)`**
   Returns the number of elements in the list.

   ```python
   print(len(l1))  # 6
   ```

   **Roman Urdu:** `len()` list ke total elements return karta hai.

8. **`max(list)`**
   Returns the maximum value from the list.

   ```python
   print(max(l1))  # 15
   ```

   **Roman Urdu:** `max()` list ka sabse bada value find karta hai.

9. **`min(list)`**
   Returns the minimum value from the list.

   ```python
   print(min(l1))  # 1
   ```

   **Roman Urdu:** `min()` list ka sabse chhota value return karta hai.

10. **`sum(list)`**
    Returns the sum of all elements in the list.

    ```python
    print(sum(l1))  # 39
    ```

    **Roman Urdu:** `sum()` list ke tamam elements ka total calculate karta hai.

11. **`list.copy()`**
    Creates a copy of the list.

    ```python
    l2 = l1.copy()
    print(l2)  # [15, 8, 7, 8, 1]
    ```

    **Roman Urdu:** `copy()` se list ki duplicate copy banayi jati hai.

12. **`list.extend(iterable)`**
    Adds all elements of another iterable to the list.

    ```python
    l2 = [20, 25]
    l1.extend(l2)
    print(l1)  # [15, 8, 7, 8, 1, 20, 25]
    ```

    **Roman Urdu:** `extend()` se list ke end par aur elements add kiye jate hain.

---

## TUPLES IN PYTHON

A tuple is an immutable data type in Python.

```python
a = ()         # empty tuple
a = (1,)       # tuple with only one element
b = (1, 7, 2)  # tuple with more than one element
```

### TUPLE METHODS

Consider the following tuple:

```python
t1 = (1, 2, 3, 4, 2, 5, 6)
```

1. **`len(tuple)`**
   Returns the total number of elements in the tuple.

   ```python
   print(len(t1))  # Output: 7
   ```

   **Roman Urdu:** `len()` tuple ke total elements batata hai.

2. **`max(tuple)`**
   Returns the maximum value in the tuple.

   ```python
   print(max(t1))  # Output: 6
   ```

   **Roman Urdu:** `max()` tuple ka sabse bada value return karta hai.

3. **`min(tuple)`**
   Returns the minimum value in the tuple.

   ```python
   print(min(t1))  # Output: 1
   ```

   **Roman Urdu:** `min()` tuple ka sabse chhota value return karta hai.

4. **`tuple.index(value)`**
   Returns the index of the first occurrence of the value.

   ```python
   print(t1.index(4))  # Output: 3
   ```

   **Roman Urdu:** `index()` kisi value ka pehla position return karta hai.

5. **`tuple.count(value)`**
   Returns the count of the value's occurrences in the tuple.

   ```python
   print(t1.count(2))  # Output: 2
   ```

   **Roman Urdu:** `count()` batata hai ke ek value tuple mein kitni baar aayi hai.

---

### NOTE:

- Lists are **mutable**: elements can be changed.
- Tuples are **immutable**: elements cannot be changed.


