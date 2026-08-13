codomax-module-1-ai-python/
│
├── README.md
├── 01_hello_python.py
├── 02_basic_calculator.py
├── 03_conditions_and_loops.py
├── 04_functions.py
├── 05_lists_tuples_dictionaries.py
└── 06_simple_ai_example.py

# CodoMax Module 1
# Introduction to Python

name = input("Enter your name: ")

print("Hello", name)
print("Welcome to Python programming!")

# Basic Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero.")

# Conditions and Loops

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("\nNumbers from 1 to 10:")

for i in range(1, 11):
    print(i)

# Functions in Python

def calculate_square(number):
    return number * number


num = float(input("Enter a number: "))

result = calculate_square(num)

print("Square:", result)

# Python Data Structures

# List
languages = ["Python", "C", "Java", "JavaScript"]

print("Languages:", languages)

# Tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Dictionary
student = {
    "name": "Sahithi",
    "branch": "CSE (AI & ML)",
    "module": 1
}

print("Student Details:")
print("Name:", student["name"])
print("Branch:", student["branch"])
print("Module:", student["module"])
# Simple AI-style Example
# Rule-based decision system

weather = input("Enter weather (sunny/rainy): ").lower()

if weather == "sunny":
    print("Recommendation: You can go outside.")
elif weather == "rainy":
    print("Recommendation: Carry an umbrella.")
else:
    print("Recommendation: Weather information not recognized.")
