"""
Question 11

Title:
Check Whether a Number is a Multiple of 7

Problem Statement:
Write a Python program to check whether a number is a multiple of 7.

Expected Output:
Enter a number: 49

49 is a multiple of 7.

Difficulty:
Beginner

Concepts:
- if
- else
- Modulus Operator (%)
"""

# Solution starts here

number = int(input("Enter a number: "))

if number % 7 == 0:
    print(number, "is a multiple of 7.")
else:
    print(number, "is not a multiple of 7.")