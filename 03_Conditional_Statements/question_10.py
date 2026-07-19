"""
Question 10

Title:
Check Character Type

Problem Statement:
Write a Python program to check whether an entered character is a vowel or a consonant.

Expected Output:
Enter a character: a

'a' is a Vowel.

Difficulty:
Beginner

Concepts:
- if
- else
- Logical Operator (or)
"""

# Solution starts here

char = input("Enter a character: ").lower()

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print(f"'{char}' is a Vowel.")
else:
    print(f"'{char}' is a Consonant.")