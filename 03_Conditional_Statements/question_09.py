"""
Question 09

Title:
Check Divisibility by 3 and 5

Problem Statement:
Write a Python program to check whether a number is divisible by both 3 and 5.

Expected Output:
Enter a number: 30

30 is divisible by both 3 and 5.

Difficulty:
Beginner

Concepts:
- if
- else
- Logical Operator (and)
"""

# Solution starts here

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(number, "is divisible by both 3 and 5.")
else:
    print(number, "is not divisible by both 3 and 5.")