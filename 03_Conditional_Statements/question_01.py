"""
Question 01

Title:
Check Positive, Negative or Zero

Problem Statement:
Write a Python program to check whether a number is positive, negative or zero.

Expected Output:
Enter a number: -5

The number is Negative.

Difficulty:
Beginner

Concepts:
- if
- elif
- else
- Comparison Operators
"""

# Solution starts here

number = int(input("Enter a number: "))

if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")