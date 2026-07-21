"""
Question 20

Title:
Simple Calculator Using if-elif

Problem Statement:
Write a Python program to perform addition, subtraction, multiplication and division based on the user's choice.

Expected Output:
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): *

Result = 50

Difficulty:
Intermediate

Concepts:
- if
- elif
- else
- Arithmetic Operators
"""

# Solution starts here

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid Operator")