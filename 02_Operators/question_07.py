"""
Question 07

Title:
Find the Power

Problem Statement:
Write a Python program to take two numbers as input and print the result of num1 raised to the power of num2.

Expected Output:
Enter base: 2
Enter exponent: 5
Result = 32

Difficulty:
Beginner

Concepts:
- Variables
- input()
- int()
- Exponent Operator (**)
"""

# Solution starts here

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = base ** exponent

print("Result =", result)