"""
Question 11

Title:
Return the Sum of Two Numbers

Problem Statement:
Write a Python function that accepts two numbers and returns their sum.

Expected Output:
Enter first number: 10
Enter second number: 20

Sum = 30

Difficulty:
Beginner

Concepts:
- return
- Function
"""

# Solution starts here

def add(num1, num2):
    return num1 + num2

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

result = add(first, second)

print("Sum =", result)