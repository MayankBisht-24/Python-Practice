"""
Question 04

Title:
Find the Greater Number

Problem Statement:
Write a Python program to find the greater of two numbers.

Expected Output:
Enter first number: 50
Enter second number: 30

Greater Number = 50

Difficulty:
Beginner

Concepts:
- if
- else
- Comparison Operators
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greater Number =", num1)
else:
    print("Greater Number =", num2)