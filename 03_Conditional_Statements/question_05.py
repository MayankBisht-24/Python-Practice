"""
Question 05

Title:
Check Divisibility

Problem Statement:
Write a Python program to check whether a number is divisible by 5.

Expected Output:
Enter a number: 25

25 is divisible by 5.

Difficulty:
Beginner

Concepts:
- if
- else
- Modulus Operator (%)
"""

# Solution starts here

number = int(input("Enter a number: "))

if number % 5 == 0:
    print(number, "is divisible by 5.")
else:
    print(number, "is not divisible by 5.")