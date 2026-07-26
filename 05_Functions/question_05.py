"""
Question 05

Title:
Function to Find the Square of a Number

Problem Statement:
Write a function that accepts a number and prints its square.

Expected Output:
Enter a number: 8

Square = 64

Difficulty:
Beginner

Concepts:
- Parameters
- Arithmetic Operators
"""

# Solution starts here

def square(number):
    print("Square =", number ** 2)

num = int(input("Enter a number: "))

square(num)