# Problem 1: Print Twinkle Twinkle Little Star Poem
# Roman Urdu Explanation:
# Yeh program ek poem print karega multi-line string ke zariye jo triple quotes ''' ya """ se likhi jati hai.

print('''
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
''')

# Problem 2: Print Table of 5 using Python as a Calculator in REPL (Read-Eval-Print Loop)
# Roman Urdu Explanation:
# Python ka REPL use karte hue, har step ko manually likhte hain jaise calculator mein.
# Yeh lines REPL mein execute karen:
# 5 * 1
# 5 * 2
# 5 * 3
# aur isi tarah 5 * 10 tak manually likhein aur result dekhein.

# Problem 3: Use External Module (pyttsx3)
# Roman Urdu Explanation:
# Pyttsx3 ek external module hai jo text-to-speech conversion ke liye use hota hai. Install karne ke liye:
# `pip install pyttsx3`. Yeh program "My name is Shaheer Ahmad" ko awaaz mein bolta hai.

import pyttsx3
engine = pyttsx3.init()
engine.say("My name is Shaheer Ahmad")  # Text ko speech mein convert karega.
engine.runAndWait()  # Awaaz sunane ke liye function call hota hai.

# Problem 4: Print Directory Contents Using `os` Module
# Roman Urdu Explanation:
# Is program mein hum `os` module use karte hain directory ke contents (files aur folders) list karne ke liye.

import os

directory_path = "."  # Current directory ko specify karte hain.
contents = os.listdir(directory_path)  # Directory ke contents ki list banate hain.

for item in contents:  # Har item ko loop mein process karte hain.
    print(item)  # File ya folder ka naam print hota hai.

# Problem 5: Label Program from Problem 4 with Comments
# Roman Urdu Explanation:
# Is program mein har step ko comments ke zariye explain kiya gaya hai.

import os  # Yahan hum os module ko import karte hain jo directory handling ke liye hota hai.

directoryPath = "."  # "Current directory" ka path specify karte hain.

# `os.listdir()` ek function hai jo directory ke contents (files aur folders) ko list mein convert karta hai.
content = os.listdir(directoryPath)

for product in content:  # For loop har file ya folder ka naam print karta hai.
    print(product)
