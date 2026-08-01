"""
Question 08

Title:
Check Palindrome String

Problem Statement:
Write a Python program to check whether a string is a palindrome.

Expected Output:
Enter a string: madam

The string is a Palindrome.

Difficulty:
Beginner

Concepts:
- String Slicing
- if-else
"""

# Solution starts here

text = input("Enter a string: ").lower()

if text == text[::-1]:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")