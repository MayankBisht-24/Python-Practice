"""
Question 10

Title:
Swap Two Numbers (Without Third Variable)

Problem Statement:
Write a Python program to swap two numbers without using a third variable.

Expected Output:
Enter first number: 15
Enter second number: 25

After Swapping

First Number = 25
Second Number = 15

Difficulty:
Beginner

Concepts:
- Variables
- Assignment Operator
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1, num2 = num2, num1

print("\nAfter Swapping")
print("First Number =", num1)
print("Second Number =", num2)
