"""
Question 14

Title:
Return Whether a Number is Even

Problem Statement:
Write a Python function that returns True if the number is even, otherwise False.

Expected Output:
Enter a number: 12

True

Difficulty:
Beginner

Concepts:
- return
- Boolean
"""

# Solution starts here

def is_even(number):
    return number % 2 == 0

num = int(input("Enter a number: "))

print(is_even(num))