"""
Question 16

Title:
Check Whether a Year is a Leap Year (Complete Logic)

Problem Statement:
Write a Python program to check whether a given year is a leap year.

Rules:
- Divisible by 400 → Leap Year
- Divisible by 100 but not 400 → Not Leap Year
- Divisible by 4 but not 100 → Leap Year
- Otherwise → Not Leap Year

Expected Output:
Enter a year: 2000

2000 is a Leap Year.

Difficulty:
Intermediate

Concepts:
- if
- elif
- else
- Nested Conditions
"""

# Solution starts here

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year.")
elif year % 100 == 0:
    print(year, "is not a Leap Year.")
elif year % 4 == 0:
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")