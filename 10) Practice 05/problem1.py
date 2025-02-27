# problem 1
''' Write a program to create a dictionary of Urdu words with values as their English translation. Provide user with an option to look it up!'''

words={
    "pankha":"fan",
    "aalu":"potato",
    "kursi":"chair",
    "gaari":"car"
}
word=input("wo word likho jiska matlb chahiye : ")
print(f"{word} ka matlab hay {words[word]}")