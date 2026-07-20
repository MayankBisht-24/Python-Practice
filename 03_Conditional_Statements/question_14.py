"""
Question 14

Title:
Check Number is Within Range

Problem Statement:
Write a Python program to check whether a number lies between 1 and 100 (inclusive).

Expected Output:
Enter a number: 75

75 is within the range.

Difficulty:
Beginner

Concepts:
- if
- else
- Logical Operator (and)
"""

# Solution starts here

number = int(input("Enter a number: "))

if number >= 1 and number <= 100:
    print(number, "is within the range.")
else:
    print(number, "is outside the range.")