"""
Question 07

Title:
Reverse a String

Problem Statement:
Write a Python program to reverse a given string.

Expected Output:
Enter a string: Python

Reversed String = nohtyP

Difficulty:
Beginner

Concepts:
- String Slicing
"""

# Solution starts here

text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed String =", reversed_text)