"""
Question 06

Title:
Function to Find the Cube of a Number

Problem Statement:
Write a Python function that accepts a number and prints its cube.

Expected Output:
Enter a number: 4

Cube = 64

Difficulty:
Beginner

Concepts:
- Function
- Parameters
- Exponent Operator (**)
"""

# Solution starts here

def cube(number):
    print("Cube =", number ** 3)

num = int(input("Enter a number: "))

cube(num)