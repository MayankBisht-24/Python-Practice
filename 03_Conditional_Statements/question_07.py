"""
Question 07

Title:
Check Pass or Fail

Problem Statement:
Write a Python program to check whether a student has passed or failed.
Passing marks are 33.

Expected Output:
Enter marks: 65

Result: Pass

Difficulty:
Beginner

Concepts:
- if
- else
- Comparison Operators
"""

# Solution starts here

marks = int(input("Enter marks: "))

if marks >= 33:
    print("Result: Pass")
else:
    print("Result: Fail")