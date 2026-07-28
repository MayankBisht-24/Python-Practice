"""
Question 12

Title:
Return the Square of a Number

Problem Statement:
Write a Python function that returns the square of a number.

Expected Output:
Enter a number: 8

Square = 64

Difficulty:
Beginner

Concepts:
- return
- Function
"""

# Solution starts here

def square(number):
    return number ** 2

num = int(input("Enter a number: "))

result = square(num)

print("Square =", result)