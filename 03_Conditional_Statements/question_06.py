"""
Question 06

Title:
Check Leap Year

Problem Statement:
Write a Python program to check whether a given year is a leap year or not.

Expected Output:
Enter a year: 2024

2024 is a Leap Year.

Difficulty:
Beginner

Concepts:
- if
- else
- Modulus Operator (%)
"""

# Solution starts here

year = int(input("Enter a year: "))

if year % 4 == 0:
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")