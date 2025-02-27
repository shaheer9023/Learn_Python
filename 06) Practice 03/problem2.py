# problem 2
# Write a program to fill in a letter template given below with name and date.
letter = ''' Dear <|Name|>,
 You are selected!
   <|Date|> '''

print(letter.replace("<|Name|>", "Shaheer Ahmad").replace(
    "<|Date|>", "December 16,2024"))
