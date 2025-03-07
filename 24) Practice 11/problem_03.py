"""Create a class ‘Employee’ and add salary and increment properties to it."""
"""Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary."""


class Employee:
    salary = 5000
    increment = ((20)/100)  # 20%

    @property
    def salaryAfterIncrement(self):
        self.Salary = (self.salary)+(self.salary*self.increment)
        return (f"salary after 20 % increment is {self.Salary}")

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary-self.salary)/self.salary)


e = Employee()
print("-"*50)
print(f"initial salary is {e.salary}")
print("-"*50)
print(e.salaryAfterIncrement)
print("-"*50)
new_salary = int(input("enter new salary : "))
e.salaryAfterIncrement = new_salary

print(f"total increment = {e.increment * 100} %")
print("-"*50)
