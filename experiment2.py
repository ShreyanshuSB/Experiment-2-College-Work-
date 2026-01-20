# 1:This is a single-line comment


"""
This is a multi-line comment (docstring).
It can be used to explain what the program does.
"""

print("Hello Python!")
print("This example shows how comments work in a program.")


# 2:Variable Declaration + Data Types
employee_name = "Rahul"
salary = 55000
rating = 4.7
is_permanent = False

print("Name:", employee_name, "Type:", type(employee_name))
print("Salary:", salary, "Type:", type(salary))
print("Rating:", rating, "Type:", type(rating))
print("Permanent Employee:", is_permanent, "Type:", type(is_permanent))


# 3) Arithmetic, Relational, Logical, Assignment & Bitwise Operators
x = 12
y = 7

# Arithmetic Operators
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)

# Relational Operators
print("x < y:", x < y)
print("x != y:", x != y)

# Logical Operators
print("AND:", x > 10 and y > 5)
print("OR:", x < 5 or y > 5)
print("NOT:", not(x == y))

# Assignment Operators
z = x
z *= y
print("Assignment Result:", z)

# Bitwise Operators
print("Bitwise AND:", x & y)
print("Bitwise XOR:", x ^ y)


# 4) Input + Formatted Output using input() and print()
city = input("Enter your city: ")
year = int(input("Enter your birth year: "))

age = 2026 - year

print("City:", city)
print("Your Age is:", age)
