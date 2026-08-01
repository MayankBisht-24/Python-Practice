"""
Question 10

Title:
Count the Occurrences of a Character

Problem Statement:
Write a Python program to count how many times a character appears in a string.

Expected Output:
Enter a string: banana
Enter a character: a

Occurrences = 3

Difficulty:
Beginner

Concepts:
- for loop
- Strings
"""

# Solution starts here

text = input("Enter a string: ").lower()
character = input("Enter a character: ").lower()

count = 0

for ch in text:
    if ch == character:
        count += 1

print("Occurrences =", count)