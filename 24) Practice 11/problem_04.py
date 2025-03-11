"""Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them."""


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    

c1=Complex(33,23)
c2=Complex(44,87)
print(c1+c2)
print(c1*c2)

"""# 🔥 User se jitne chahe values lo!
objects = []
n = int(input("Kitne complex numbers enter karna chahte hain? "))
for i in range(n):
    real = int(input(f"Enter real part {i+1}: "))
    imaginary = int(input(f"Enter imaginary part {i+1}: "))
    objects.append(Complex(real, imaginary))

# ✅ Pehla object base value banega
sum_result = objects[0]
product_result = objects[0]

# 🔄 Baaki numbers ko add aur multiply karo
for obj in objects[1:]:  # Pehle wale ko chhod kar aage walon ko process karo
    sum_result += obj
    product_result *= obj

print("\nTotal Sum:", sum_result)
print("Total Product:", product_result)"""