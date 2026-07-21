"""
Question 18

Title:
Check Character is Alphabet or Not

Problem Statement:
Write a Python program to check whether the entered character is an alphabet.

Expected Output:
Enter a character: A

It is an alphabet.

Difficulty:
Intermediate

Concepts:
- if
- else
- Comparison Operators
"""

# Solution starts here

char = input("Enter a character: ")

if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")