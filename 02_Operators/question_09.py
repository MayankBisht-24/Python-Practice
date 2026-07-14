"""
Question 09

Title:
Swap Two Numbers (Using Third Variable)

Problem Statement:
Write a Python program to swap two numbers using a third variable.

Expected Output:
Enter first number: 10
Enter second number: 20

After Swapping

First Number = 20
Second Number = 10

Difficulty:
Beginner

Concepts:
- Variables
- input()
- Assignment Operator
"""

# Solution starts here

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp

print("\nAfter Swapping")
print("First Number =", num1)
print("Second Number =", num2)