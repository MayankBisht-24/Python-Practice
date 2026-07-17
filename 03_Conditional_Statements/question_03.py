"""
Question 03

Title:
Check Voting Eligibility

Problem Statement:
Write a Python program to check whether a person is eligible to vote.

Expected Output:
Enter your age: 20

You are eligible to vote.

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
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")