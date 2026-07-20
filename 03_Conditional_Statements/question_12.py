"""
Question 12

Title:
Check Eligible for Driving License

Problem Statement:
Write a Python program to check whether a person is eligible for a driving license.
Minimum age required is 18 years.

Expected Output:
Enter your age: 21

You are eligible for a driving license.

Difficulty:
Beginner

Concepts:
- if
- else
- Comparison Operators
"""

# Solution starts here

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")