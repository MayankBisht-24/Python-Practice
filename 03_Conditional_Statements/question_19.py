"""
Question 19

Title:
Check Character is Uppercase or Lowercase

Problem Statement:
Write a Python program to check whether the entered alphabet is uppercase or lowercase.

Expected Output:
Enter an alphabet: G

Uppercase Letter

Difficulty:
Intermediate

Concepts:
- if
- elif
- Comparison Operators
"""

# Solution starts here

char = input("Enter an alphabet: ")

if 'A' <= char <= 'Z':
    print("Uppercase Letter")
elif 'a' <= char <= 'z':
    print("Lowercase Letter")
else:
    print("Invalid Input")