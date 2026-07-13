"""
Question 05

Title:
Find the Remainder

Problem Statement:
Write a Python program to take two numbers as input and print the remainder after division.

Expected Output:
Enter first number: 17
Enter second number: 5
Remainder = 2

Difficulty:
Beginner

Concepts:
- Variables
- input()
- int()
- Modulus Operator (%)
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

remainder = num1 % num2

print("Remainder =", remainder)