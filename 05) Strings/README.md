# Strings in Python 



String is a data type in Python. A string is a sequence of characters enclosed in quotes. We can write a string in these three ways:


```python
a = 'shaheer'    # Single quoted string
b = "shaheer"   # Double quoted string
c = '''shaheer''' # Triple quoted string
```

### STRING SLICING

A string in Python can be sliced to get a part of the string. Consider the following string:

#### String Indexing
The index in a string starts from 0 to (length - 1). Here is an example:

```
Name = "shaheer"
# Indexes:   0   1   2   3   4   5   6
# Letters:   s   h   a   h   e   e   r
# Negative: -7  -6  -5  -4  -3  -2  -1
```

#### String Slicing Syntax:
```python
slice = name[start_index : end_index]
```
- **Start Index**: Included
- **End Index**: Not Included

**Example:**
```python
Name = "shaheer"
slice1 = Name[0:3]   # Returns 'sha'
slice2 = Name[1:4]   # Returns 'hah'
```

#### Negative Indices:
Negative indices allow us to count from the end of the string.
```python
Name = "shaheer"
slice3 = Name[-7:-4]  # Returns 'sha'
```

### SLICING WITH SKIP VALUE
We can use a skip value in the slice to skip certain characters:
```python
word = "amazing"
print(word[1:6:2])  # Returns 'mzn'
```

Other examples:
```python
word = "amazing"
print(word[:7])  # Same as word[0:7], returns 'amazing'
print(word[0:])  # Same as word[0:7], returns 'amazing'
```

### STRING FUNCTIONS
Here are some commonly used string functions with code examples:

1. **Length of String (`len`)**:
```python
name = "shaheer ahmad"
print(len(name))  # Returns 13
```

2. **Ends With (`endswith`)**:
```python
print(name.endswith("ahmad"))  # Returns True
```

3. **Starts With (`startswith`)**:
```python
print(name.startswith("shaheer"))  # Returns True
```

4. **Replace Characters (`replace`)**:
```python
print(name.replace("ahmad", "ali"))  # Returns 'shaheer ali'
```

5. **Convert to Title Case (`title`)**:
```python
print(name.title())  # Returns 'Shaheer Ahmad'
```

6. **Capitalize First Letter (`capitalize`)**:
```python
print(name.capitalize())  # Returns 'Shaheer ahmad'
```

7. **Convert to Uppercase (`upper`)**:
```python
print(name.upper())  # Returns 'SHAHEER AHMAD'
```

8. **Convert to Lowercase (`lower`)**:
```python
print(name.lower())  # Returns 'shaheer ahmad'
```

9. **Find Index of Substring (`find`)**:
```python
print(name.find("ahmad"))  # Returns 8
```

10. **Count Occurrences of a Character (`count`)**:
```python
print(name.count("a"))  # Returns 3
```

### ESCAPE SEQUENCE CHARACTERS
Escape sequence characters are used to represent special characters in strings:

1. **Newline (`\n`)**:
```python
print("Shaheer\nAhmad")
# Output:
# Shaheer
# Ahmad
```

2. **Tab (`\t`)**:
```python
print("Shaheer\tAhmad")
# Output:
# Shaheer   Ahmad
```

3. **Backslash (`\\`)**:
```python
print("This is a backslash: \\")  # Output: This is a backslash: \
```
