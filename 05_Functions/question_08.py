"""
Question 08

Title:
Function to Find the Largest of Two Numbers

Problem Statement:
Write a Python function that accepts two numbers and prints the larger number.

Expected Output:
Enter first number: 30
Enter second number: 50

Largest Number = 50

Difficulty:
Beginner

Concepts:
- Function
- Parameters
- if-else
"""

# Solution starts here

def largest(num1, num2):
    if num1 > num2:
        print("Largest Number =", num1)
    else:
        print("Largest Number =", num2)

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

largest(first, second)